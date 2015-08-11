carthage-copy-frameworks
========================

[![PyPI Version](https://img.shields.io/pypi/v/carthage-copy-frameworks.svg)](https://pypi.python.org/pypi/carthage-copy-frameworks)
[![PyPI Downloads](https://img.shields.io/pypi/dm/carthage-copy-frameworks.svg)](https://pypi.python.org/pypi/carthage-copy-frameworks)
[![MIT License](https://img.shields.io/badge/license-mit-blue.svg)](http://choosealicense.com/licenses/mit/)


# Overview

`carthage-copy-frameworks` is an helper script that you can use to automatically copy every
framework below `Carthage/Build/iOS`. This way you can avoid [the official, error prone,
process](https://github.com/Carthage/Carthage#if-youre-building-for-ios).

As the name implies, this is meant to be used in iOS development, alongside
[Carthage](https://github.com/Carthage/Carthage).


# Installation

If you are on OS X and have Homebrew's Python:

    pip install carthage-copy-frameworks

Otherwise:

    pip install --user carthage-copy-frameworks

Then make sure to add the local pip's `bin` directory to the `$PATH`. Since it is different on each
platform, please refer to its documentation.

Otherwise, if you're feeling a badass and want to `sudo` your way out, then run:

    sudo pip install carthage-copy-frameworks


# Usage

1. Open your target configuration.
2. Click on "Build Phases".
3. Click on the plus ("+") button.

![Step 1](images/step1.png)

-----

Click on "New Run Script Phase"

![Step 2](images/step2.png)

-----

In the script text field type `carthage-copy-frameworks`, as shown in the picture.

![Step 3](images/step3.png)


# Notes

Frameworks are not copied over and over again. This means that updated dependencies might not be
picked up until you perform a clean build.
