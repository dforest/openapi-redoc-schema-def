from setuptools import setup

setup(
    name='openapi-redoc-schema-def',
    version='0.1.1',
    install_requres=['PyYAML'],
    packages=["openapi_redoc_schema_def"],
    entry_points={
        'console_scripts': [
            "openapi-redoc-schema-def=openapi_redoc_schema_def.main:main"
        ]
    }
)
