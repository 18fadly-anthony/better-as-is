#!/usr/bin/env python

# A Better As-Is Parser

import os
import sys
import argparse

verbose = False


def read_file_to_array(filename):
    content_array = []
    with open(filename) as f:
        for line in f:
            content_array.append(line.strip('\n'))
        return(content_array)


def get_status(line):
    result = []
    statusline = line.split(' ')
    statusnum = result.append(statusline[1])
    result.append(statusline[2])
    return result


def parse_as_is(file):
    result = []
    data = read_file_to_array(file)
    result.append(get_status(data[0]))
    return result


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
        exit()

    if args.input == None:
        print("Error: no input file specified")
        print("Use -i filename")
        print("Use -h for more")
        exit()

    elif os.path.exists(args.input[0]):
        data = parse_as_is(args.input[0])
        print(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
