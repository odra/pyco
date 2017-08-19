#!/usr/bin/env python                                                                                                                               
from setuptools import setup, find_packages


setup(
  name='pyco',
  version='0.1.0',
  description='Manages and builds code and function objects.',
  author='Leonardo Rossetti',
  author_email='me@lrossetti.com',
  url='https://github.com/odra/pyco',
  packages=find_packages(),
  install_requires=[
    'six==1.10.0',
    'schematics==1.1.1'
  ],
  tests_require=['pytest', 'pytest-sugar'],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only'
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ]
)
