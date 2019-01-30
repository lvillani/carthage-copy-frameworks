#!/usr/bin/env python3

from setuptools import setup

setup(
    name="carthage-copy-frameworks",
    version="2.0.0",
    description="carthage-copy-frameworks is an helper script that automatically copies every framework below Carthage/Build/iOS",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lvillani/carthage-copy-frameworks",
    author="Lorenzo Villani",
    author_email="lorenzo@villani.me",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="apple build carthage helper ios",
    packages=["carthage_copy_frameworks"],
    entry_points={"console_scripts": ["carthage-copy-frameworks=carthage_copy_frameworks:main"]},
)
