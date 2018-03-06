#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='expire',
    version='0.0.1',
    description="Expire aims to make using cache as convenient as possible.",
    install_requires=['colorama', 'pymemcache', 'redis'],
    author='Howie Hu',
    author_email='xiaozizayang@gmail.com',
    url="https://github.com/howie6879/expire",
    packages=find_packages(),
)
