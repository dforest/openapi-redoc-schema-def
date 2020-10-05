import os
import argparse

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def main():
    args = parse_argument()

    data = load_yaml(args.path)
    schemas = data.get('components', {}).get('schemas')

    sources = {}

    for k, v in schemas.items():
        for tag in v.get('x-tags', []):
            if tag in args.tags:
                sources.setdefault(tag, [])
                sources.get(tag).append({'key': k, 'title': v.get('title', k)})

    tags = data.get('tags')
    for tag in tags:
        description = [tag.get('description', None)]
        for source in sources.get(tag.get('name', ''), []):
            description.append('## {}'.format(source.get('title')))
            description.append('<SchemaDefinition schemaRef="#/components/schemas/{}" />'.format(source.get('key')))
            description.append('')
        tag['description'] = '\n'.join(list(filter(None, description)))

    write_to_yaml(data, args.path)


def load_yaml(path):
    with open(path) as f:
        return yaml.load(f, Loader=Loader)

def write_to_yaml(data, path):
    with open(path, 'w') as f:
        f.write(yaml.dump(data, Dumper=Dumper))

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        path=None,
        tags=[]
    )

    parser.add_argument(
        '--path',
        required=True,
        help="Path to file"
    )
    parser.add_argument(
        '--tags',
        required=True,
        nargs='+',
        help="Array of tag for schema defition"
    )
    args = parser.parse_args()

    if not os.path.exists(args.path):
        parser.error(f'{args.path} is not exists')

    return args

if __name__ == "__main__":
    main()
