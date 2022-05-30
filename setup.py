"""Redis bridge setup script."""

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pyRedisBridge',
    version='0.1.0',
    license='MIT',
    url='https://github.com/sourceperl/pyRedisBridge',
    platforms='any',
    install_requires=required,
    scripts=[
        'redis-serial-sync'
    ]
)
