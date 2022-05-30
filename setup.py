"""Redis bridge setup script."""

import pyRedisBridge
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pyRedisBridge',
    version=pyRedisBridge.__version__,
    license=pyRedisBridge.__license__,
    url=pyRedisBridge.__url__,
    platforms='any',
    install_requires=required,
    packages=['pyRedisBridge'],
    scripts=[
        'redis-serial-sync'
    ]
)
