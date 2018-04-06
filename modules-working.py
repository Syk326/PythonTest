#!/usr/bin/env python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# modules in Standard Library, check through
import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    # can import within function, i.e. do things one way or another depending on the platform
    import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd()) # current working dir

    import random
    print(random.randint(1,1000)) # random num between 1-1000
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

    # THIRD-PARTY
    # read doc and source code, try out - don't reinvent wheel!
    import bitstring
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.uint)

if __name__ == "__main__": main()
