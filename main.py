#!/usr/bin/env python

# A Better As-Is Parser

import os
import sys
import argparse

verbose = False


def parse_as_is():
    return True


def main():
    global verbose

    # ArgParse

    parser = argparse.ArgumentParser(
        description = '''As-Is Parser''',
        epilog = '''Copyright (c) 2021 Anthony Fadly'''
    )

    parser.add_argument('-i', '--input', metavar = '<file>', nargs = 1, type = str, default = [None], help = "Specify input file")
    parser.add_argument('-o', '--output', metavar = '<path>', nargs = 1, type = str, default = [None], help = "Optionally specify output file instead of stdout")
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Be verbose')

    args = parser.parse_args()

    verbose = args.verbose

    # No argument
    if len(sys.argv) == 1:
        print("Error: no option specified")
        print("Use -i filename")
        print("Use -h for more")

    if args.input == None:
        print("Error: no input file specified")
        print("Use -i filename")
        print("Use -h for more")
    elif os.path.exist(args.input):
        data = parse_as_is(args.input)
        print(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
