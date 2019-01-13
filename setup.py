# -*- coding: utf-8 -*-

# z setup

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='bin',
    version='1.0.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Rich Bateman',
    author_email='integrations@ncino.com',
    url='tbd',
    packages=find_packages(exclude=('tests', 'docs'))
)
