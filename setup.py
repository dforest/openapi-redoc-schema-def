from setuptools import setup

setup(
    name='openapi-redoc-schema-def',
    version='0.1.0',
    install_requres=['PyYAML'],
    entry_points={
        'console_scripts': [
            "openapi-redoc-schema-def=main:main"
        ]
    }
)
