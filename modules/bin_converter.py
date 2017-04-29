#!/usr/bin/env python3

# This is a library from my other project binary_converter, see full project here: <url>
# Copyright (C) 2017 ArenGamerZ

import sys, re

def check(ip):
    """ This function checks whether a given IP is valid or not """

    patt = re.compile("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$")
    if re.match(patt, ip):
        # In python a '1' means True
        return 1
    else:
        # In python a '0' means False
        return 0


def convert(ip, format="decimal"):
    """ This function does all the magic of converting the given IP address into a bynary IP address
        Arguments:
            ip = Originally the IP passed to the function, now it can be a numbrer too
            format = The format of the number given: 'decimal' or 'binary'"""

    # If you wonder why I do not use bin(ip) it's because bin() does not return the result in 8 bit format, and that makes it look pretty ugly
    result = []
    if format == "decimal":
        if check(ip):
            for group in ip.split('.'):
                group_result = []
                number = 128
                # 8 = 128 64 32 16 8 4 2 1
                for i in range(8):
                    group = int(group)
                    if group >= number:
                        group_result.append('1')
                        group = group-number
                    else:
                        group_result.append('0')
                    number = number/2
                group_result = ''.join(group_result)
                result.append(group_result)
            return '.'.join(result)
        else:
            if int(ip):
                number = 128
                for i in range(8):
                    ip = int(ip)
                    if ip >= number:
                        result.append('1')
                        ip = ip - number
                    else:
                        result.append('0')
                    number = number/2
                return ''.join(result)
    elif format == "binary":
        if check(ip):
            for group in ip.split('.'):
                result.append(str(int(group, 2)))
            return '.'.join(result)
        else:
            return str(int(ip, 2))


# If it is not the main process (e.g.: imported), the program will not seek for parameters
if __name__ == "__main__":
    print(fcolors.RED+"Error: This module is not meant to be excecuted!!!"+fcolors.RESET)
    exit(1)
