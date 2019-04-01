# carthage-copy-frameworks

![Version](https://img.shields.io/badge/version-v2.0.0-blue.svg)
[![MIT License](https://img.shields.io/badge/license-mit-blue.svg)](http://choosealicense.com/licenses/mit/)


# Overview

`carthage-copy-frameworks` is an helper script that you can use to automatically copy every
framework below `Carthage/Build/iOS`. This way you can avoid [the official, error prone,
process](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).

As the name implies, this is meant to be used in iOS development, alongside
[Carthage](https://github.com/Carthage/Carthage).


# Installation

    brew install lvillani/tap/carthage-copy-frameworks


# Usage

1. Open your target configuration.
2. Click on "Build Phases".
3. Click on the plus ("+") button.
4. Click on "New Run Script Phase"

![Step 1](images/step1.png)

----

In the script text field type `carthage-copy-frameworks`, as shown in the picture.

![Step 2](images/step2.png)


# Notes

Frameworks are copied only once. There are no checks to copy a framework again once it changes. This
means that updated dependencies might not be picked up until you perform a clean build.
