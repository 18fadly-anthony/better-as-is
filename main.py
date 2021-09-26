#!/usr/bin/env python

# A Better As-Is Parser

import os
import sys
import argparse

verbose = False
http_codes = [100,101,102,103,200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,421,422,423,424,425,426,428,429,431,451,500,501,502,503,504,505,506,507,508,510,511]


def read_file_to_array(filename):
    content_array = []
    with open(filename) as f:
        for line in f:
            content_array.append(line.strip('\n'))
        return(content_array)


def get_status(line):
    result = []
    statusline = line.split(' ')
    if len(statusline) != 3:
        print("Syntax Error on line 1:")
        print(line)
        print("Expected 3 terms")
        exit()
    if not statusline[0] == 'status:':
        print("Syntax Error on line 1:")
        print(line)
        print("Expected 'status:'")
        exit()
    try:
        statusnum = int(statusline[1])
    except ValueError:
        print("Syntax Error on line 1:")
        print(line)
        print("Expected an http status code")
        exit()
    if not statusnum in http_codes:
        print("Syntax Error on line 1:")
        print(line)
        print(str(statusnum) + " is not a valid http status code")
        exit()
    result.append(statusnum)
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
