#!/usr/bin/env python3

################################################################################################################################################
# ShortName: binary.py
# FullName: binary_converter.py
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 2.0-alpha
# Description: This is a program that will convert given IP address or a number into its binary representation
################################################################################################################################################

import sys, re, getopt
from extra_modules import colors as c


def bhelp():
    """ This function prints the help """
    print("Usage: ")
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


def convert(ip):
    """ This function does all the magic of converting the given IP address into a bynary IP address"""
    # If you wonder why I do not use bin(ip) when it's an IP it's because bin() does not return in 8 bit format, and that makes it pretty ugly
    # For instance, 192.168.12.14 will be like: 11000000.10101000.1100.1110
    if check(ip):
        result = []
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
                return bin(int(ip))[2:]
        except ValueError:
            return "That is not a valid IP address nor a number!!!"


def loop(times):
    """ This function loops to enter several IPs """
    try:
        for i in range(times):
            ip = input("Give me an IP or a number: ")
            print("Binary representation: "+convert(ip))
            print("")
    except KeyboardInterrupt:
        print("\nForced exit with 'Ctrl-C' by user")
        sys.exit(0)


# If it is not the main process (e.g.: imported), the program will not seek for parameters
if __name__ == "__main__":
    try:
        if sys.argv[1][0] != "-":
            if check(sys.argv[1]):
                print("IP in binary: "+convert(sys.argv[1]))
            else:
                try:
                    int(sys.argv[1])
                    print("Number in binary: "+convert(sys.argv[1]))
                except ValueError:
                    print("Error: Not a valid number nor IP!")
                    sys.exit(1)
        elif sys.argv[1][0] == "-":
            try:
                opts, args = getopt.getopt(sys.argv[1:], "hl:", ["help", "loop="])
            except getopt.GetoptError:
                print("Parameter Error: Use '-h' or '--help' to see the help!")
                sys.exit(1)
            for opt, arg in opts:
                if opt in ("-h", "--help"):
                    bhelp()
                    sys.exit(0)
                elif opt in ("-l", "--loop"):
                    loop(int(arg))
                    sys.exit(0)
        else:
            print("Parameter Error: Use '-h' or '--help' to see the help")
            sys.exit(1)
    except IndexError:
        print("Error: No parameters suplied!")
        bhelp()
        sys.exit(1)
