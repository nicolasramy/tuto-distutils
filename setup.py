#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import re
from setuptools import setup, find_packages

with io.open("ssl_checker/__init__.py", "rt", encoding="utf8") as file_resource:
    version = re.search(r"__version__ = \'(.*?)\'", file_resource.read()).group(1)

setup(
    name="SSL Checker",
    version=version,
    description="A simple tool to get some information about a SSL certificate",
    author="Nicolas RAMY",
    author_email="nicolas.ramy@darkelda.com",
    url="https://github.com/nicolasramy/tuto-distutils",
    license="MIT",
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ssl-checker=ssl_checker.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
)
