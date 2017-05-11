#!/usr/bin/env python
from setuptools import setup, find_packages


NAME = 'python-instagram'
VERSION = '1.3.2.7'


REQUIREMENTS = [
    'simplejson',
    'httplib2',
    'six'
]


setup(
    name=NAME,
    version=VERSION,
    description='Instagram API client',
    license='MIT',
    install_requires=REQUIREMENTS,
    author='Instagram, Inc',
    author_email='apidevelopers@instagram.com',
    url='http://github.com/sociateru/python-instagram',
    packages=find_packages(),
    keywords='instagram',
    zip_safe=True
)
