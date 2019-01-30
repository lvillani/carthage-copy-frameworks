#!/usr/bin/env python3
#
# The MIT License (MIT)
#
# Copyright (c) 2019 Lorenzo Villani
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import argparse
import os
import os.path
import subprocess
import sys
from collections import namedtuple

__version__ = "2.0.0"

HERE = os.path.abspath(os.path.dirname(__file__))

Framework = namedtuple("Framework", ["name", "path"])


def main():
    sanity_check()

    args = parse_args()

    print("carthage-copy-frameworks v{}".format(__version__))

    if args.exclude is not None:
        excluded_frameworks = args.exclude
    else:
        excluded_frameworks = []

    if args.carthage is not None:
        additional_carthage_folders = args.carthage
    else:
        additional_carthage_folders = []

    # Check for additional excluded frameworks defined in input variables
    script_input_file_count = int(os.environ["SCRIPT_INPUT_FILE_COUNT"])

    print(
        "Found",
        script_input_file_count,
        "input files to be treated as frameworks to exclude",
    )

    for i in range(0, script_input_file_count):
        script_input_file_pos = "SCRIPT_INPUT_FILE_" + str(i)
        script_input_file = os.environ[script_input_file_pos]
        framework_to_exclude = os.path.basename(script_input_file)
        print("Framework " + framework_to_exclude + " will be excluded.")
        excluded_frameworks.append(framework_to_exclude)
        # Reset variable
        del os.environ[script_input_file_pos]
    del os.environ["SCRIPT_INPUT_FILE_COUNT"]

    srcroot = os.environ["SRCROOT"]
    frameworks_dir = os.path.abspath(os.path.join(srcroot, "Carthage", "Build", "iOS"))

    additional_carthage_folders.append(frameworks_dir)

    frameworks = []

    for folder in additional_carthage_folders:
        for framework in [
            f
            for f in os.listdir(folder)
            if f.endswith(".framework") and f not in excluded_frameworks
        ]:
            frameworks.append(
                Framework(name=framework, path=os.path.join(folder, framework))
            )

    # Do we have anything to do?
    if not frameworks:
        print("No frameworks built, so nothing to copy.")
        return
    else:
        print(
            "Piping to 'carthage copy-frameworks':\n    "
            + "\n    ".join([f.name for f in frameworks])
        )

    # Export environment variables needed by Carthage as described here:
    # https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos
    os.environ["SCRIPT_INPUT_FILE_COUNT"] = str(len(frameworks))
    os.environ["SCRIPT_OUTPUT_FILE_COUNT"] = str(len(frameworks))

    for i, framework in enumerate(frameworks):
        os.environ["SCRIPT_INPUT_FILE_" + str(i)] = framework.path
        os.environ["SCRIPT_OUTPUT_FILE_" + str(i)] = (
            "$(BUILT_PRODUCTS_DIR)/$(FRAMEWORKS_FOLDER_PATH)/" + framework.name
        )

    subprocess.check_call(["carthage", "copy-frameworks"])


def sanity_check():
    must_have = ["BUILT_PRODUCTS_DIR", "FRAMEWORKS_FOLDER_PATH", "SRCROOT"]

    for envvar in must_have:
        if not envvar in os.environ:
            lines = [
                "You must launch this tool from an Xcode build step.",
                "",
                "See installation instructions at: ",
                "https://github.com/lvillani/carthage-copy-frameworks/blob/master/README.md",
            ]

            for line in lines:
                print(line)

            sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Argument Parser")
    parser.add_argument(
        "-x",
        "--exclude",
        nargs="+",
        help="Exclude dependencies from being copied",
        required=False,
    )

    parser.add_argument(
        "-c",
        "--carthage",
        nargs="+",
        help="Additional Carthage Binary Folders",
        required=False,
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
