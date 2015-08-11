#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open as open_f
from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open_f(path.join(HERE, "DESCRIPTION.rst"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="carthage-copy-frameworks",
    version="1.0.0",
    description="Keyring integration and local execution wrappers for Ansible",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/lvillani/carthage-copy-frameworks",
    author="Lorenzo Villani",
    author_email="lorenzo@villani.me",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="apple build carthage helper ios",
    packages=["ccp"],
    entry_points={
        "console_scripts": [
            "carthage-copy-frameworks=ccp:main",
        ],
    },
)
