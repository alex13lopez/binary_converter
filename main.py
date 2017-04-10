#!/usr/bin/env python3

################################################################################################################################################
# ShortName: binary.py
# FullName: binary_converter.py
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 3.0-alpha/unstable
# Description: This is a program that will convert given IP address or a number into its binary representation
# License GNU GPL
################################################################################################################################################

import argparse
from modules import colors as c
from modules import bin_converter as converter

if __name__ != __main__:
    print(c.fcolors.RED+"This module is not meant to be imported!!!")
    exit(1)
else:
    parser = argparse.ArgumentParser()
    
