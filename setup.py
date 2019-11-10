#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup, find_packages
import os
import sys

# Define the requirements and extras
requirements = [
        'matplotlib>=1.4.2',  # Plotting
        'numpy>=1.10.1',      # Numerical functions
        'dill',               # File I/O
        'gitpython',          # Version information
        'openpyexcel>=2.5',   # Spreadsheet functions -- fork of openpyxl
        'pandas',             # Spreadsheet input
        'psutil',             # Load monitoring
        'xlrd',               # Spreadsheet input
        'xlsxwriter',         # Spreadsheet output
        'requests',           # HTTP methods
        'python-Levenshtein', # For fuzzy string matching
        ]

# Optionally define extras
if 'minimal' in sys.argv:
    print('Performing minimal installation -- some file read/write functions will not work')
    sys.argv.remove('minimal')
    requirements = [
        'matplotlib>=1.4.2', # Plotting
        'numpy>=1.10.1',     # Numerical functions
    ]

# Get version
versionfile = 'sc_version.py'
versionstr = '__version__ = '
cwd = os.path.abspath(os.path.dirname(__file__))
versionpath = os.path.join(cwd, 'sciris', versionfile)
with open(versionpath, 'r') as f:
    lines = f.readlines()
    assert lines[0].startswith(versionstr)
    version = lines[0].split(versionstr)[1].rstrip()

# Get the documentation
with open("README.md", "r") as fh:
    long_description = fh.read()

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3.7',
]

setup(
    name='sciris',
    version=version,
    author='ScirisOrg',
    author_email='info@sciris.org',
    description='Scientific tools for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/sciris/sciris',
    keywords=['scientific', 'webapp', 'framework'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements
)
