#!/usr/bin/env python3

################################################################################################################################################
# ShortName: binary.py
# FullName: binary_converter.py
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 3.2.1-beta
# Description: This is a program that will convert given IP address or a number into its binary representation and viceversa
# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ
################################################################################################################################################

import argparse, sys
from modules import colors as c
from modules import bin_converter as converter


def loop(times, format="decimal"):
    """ This function loops to enter several IPs
        Arguments:
            times = The number of times program will loop
            format = The format of the number given: 'decimal' or 'binary'"""

    try:
        for i in range(times):
            ip = input(c.fcolors.GREY+"IP or number: "+c.fcolors.YELLOW)
            if format == "decimal":
                print(c.fcolors.GREY+"Binary representation: "+c.fcolors.YELLOW+converter.convert(ip)+c.fcolors.RESET)
            elif format == "binary":
                print(c.fcolors.GREY+"Decimal representation: "+c.fcolors.YELLOW+converter.convert(ip, "binary"))
            print("")
    except KeyboardInterrupt:
        print("")
        print(c.fcolors.RED+"\nAborted by user"+c.fcolors.RESET)
        sys.exit(0)


if __name__ != "__main__":
    print(c.fcolors.RED+"This module is not meant to be imported!!!"+c.fcolors.RESET)
else:
    parser = argparse.ArgumentParser(description="This is a program that will convert given IP address or a number into its binary representation and viceversa")
    conflict = parser.add_mutually_exclusive_group()
    conflict.add_argument("IP", help="IP/number to convert", type=str, nargs='?')
    parser.add_argument("-b", "--binary", action="store_true", help="Flag to specify binary format")
    conflict.add_argument("-l", "--loop", dest="times", type=int, help="(-l)oops <TIMES> times")
    args = parser.parse_args()
    try:
        if sys.argv[1]:
            if args.IP:
                if args.binary and not args.times:
                    print(c.fcolors.GREY+"Decimal representation: "+c.fcolors.YELLOW+converter.convert(args.IP, "binary")+c.fcolors.RESET)
                else:
                    print(c.fcolors.GREY+"Binary representation: "+c.fcolors.YELLOW+converter.convert(args.IP)+c.fcolors.RESET)
            else:
                if args.binary and args.times:
                    loop(args.times, "binary")
                elif args.times:
                    loop(args.times)
                else:
                    print(c.fcolors.RED+"'-b', '--binary' It's a flag, it does nothing itself"+c.fcolors.RESET)
    except IndexError:
        print(c.fcolors.RED+"No arguments given! Use '-h' to see the help"+c.fcolors.RESET)
    except ValueError:
        print(c.fcolors.RED+"That was not a valid IP Address nor a number!")
