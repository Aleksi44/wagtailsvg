#!/usr/bin/env python
import os
from setuptools import find_packages, setup
import json

PROJECT_DIR = os.path.dirname(__file__)

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('./package.json') as package:
    data = json.load(package)
    version = data['version']

setup(
    name='wagtailsvg',
    version=version,
    url='https://github.com/Aleksi44/wagtailsvg',
    author="Alexis Le Baron",
    author_email="alexis@stationspatiale.com",
    description="Wagtail SVG",
    long_description=long_description,
    keywords="wagtail svg",
    license='GPL-3.0',
    install_requires=[
        'wagtail-generic-chooser==0.1.1'
    ],
    platforms=['linux'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
