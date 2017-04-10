#!/usr/bin/env python3

################################################################################################################################################
# ShortName: binary.py
# FullName: binary_converter.py
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 3.1-beta
# Description: This is a program that will convert given IP address or a number into its binary representation and viceversa
# License GNU GPL
################################################################################################################################################

import argparse
from modules import colors as c
from modules import bin_converter as converter


if __name__ != "__main__":
    print(c.fcolors.RED+"This module is not meant to be imported!!!")
    exit(1)
else:
    parser = argparse.ArgumentParser(description="This is a program that will convert given IP address or a number into its binary representation and viceversa")
    conflict = parser.add_mutually_exclusive_group()
    conflict.add_argument("IP", help="IP/number to convert", type=str, nargs='?')
    parser.add_argument("-b", "--binary", action="store_true", help="Flag to specify binary format")
    conflict.add_argument("-l", "--loop", dest="times", type=int, help="(-l)oops <TIMES> times")
    args = parser.parse_args()

    if args.binary and not args.times:
        print(c.fcolors.GREY+"Decimal representation: "+c.fcolors.YELLOW+converter.convert(args.IP, "binary")+c.fcolors.RESET)
    elif args.binary and args.times:
        converter.loop(args.times, "binary")
    elif args.times:
        converter.loop(args.times)
    else:
        print(c.fcolors.GREY+"Binary representation: "+c.fcolors.YELLOW+converter.convert(args.IP)+c.fcolors.RESET)
