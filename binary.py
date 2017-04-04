#!/usr/bin/env python3

################################################################################################################################################
# ShortName: binary.py
# FullName: binary_converter.py
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 3.0-alpha/unstable
# Description: This is a program that will convert given IP address or a number into its binary representation
################################################################################################################################################

import sys, re, getopt
from extra_modules import colors as c


def bhelp():
    """ This function prints the help """

    print("      Usage: ")
    print("               <IP> or <number>      You must provide a valid IP with the form of X.X.X.X or a number to show the binary representation")
    print("               -l --loop <times>     Indicate how many <times> program will -(l)oop asking you IPs/numbers to convert")
    print("               -h --help             Shows this help")


def check(ip):
    """ This function checks whether a given IP is valid or not """

    patt = re.compile("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$")
    if re.match(patt, ip):
        # In python a '1' means True
        return 1
    else:
        # In python a '0' means False
        return 0


def convert(ip, nformat="decimal"):
    """ This function does all the magic of converting the given IP address into a bynary IP address
        Arguments:
            ip = Originally the IP passed to the function, now it can be a numbrer too
            nformat = The format of the number given: 'decimal' or 'binary'"""

    # If you wonder why I do not use bin(ip) it's because bin() does not return the result in 8 bit format, and that makes it look pretty ugly
    result = []
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
        try:
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
        except ValueError:
            return c.fcolors.RED+"That is not a valid IP address nor a number!!!"


def loop(times, nformat="decimal"):
    """ This function loops to enter several IPs
        Arguments:
            times = The number of times program will loop
            nformat = The format of the number given: 'decimal' or 'binary'"""

    try:
        for i in range(times):
            ip = input(c.fcolors.GREY+"IP or number: "+c.fcolors.YELLOW)
            if nformat == "decimal":
                print(c.fcolors.GREY+"Binary representation: "+c.fcolors.YELLOW+convert(ip)+c.fcolors.RESET)
            elif nformat == "binary":
                print(c.fcolors.GREY+"Decimal representation: "+c.fcolors.YELLOW+convert(ip, "binary"))
            print("")
    except KeyboardInterrupt:
        print("")
        print(c.fcolors.RED+"\nAborted by user"+c.fcolors.RESET)
        sys.exit(0)


# If it is not the main process (e.g.: imported), the program will not seek for parameters
if __name__ == "__main__":
    pass
