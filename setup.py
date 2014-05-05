# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys
import pkg_resources

sys.path.insert(0, '')
import servertest


long_description = open("README.md").read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development :: Testing",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Systems Administration",
]

requires = []
deplinks = []

setup(
    name='servertest',
    version=servertest.__version__,
    description='A Program for testing your servers configs and environments.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['test','server'],
    author='pekopeko1',
    author_email='t.moi.larsson at gmail.com',
    url='https://github.com/pekopeko1/servertest',
    download_url='http://pypi.python.org/pypi/servertest',
    license='MIT License',
    packages=find_packages(''),
    package_dir={'': ''},
    include_package_data=True,
    install_requires=requires,
    dependency_links=deplinks
)
