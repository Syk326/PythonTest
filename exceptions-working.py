#!/usr/bin/env python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

# try/except
try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
# don't have to specify error
except IOError as e:
    print("something bad happened ({})".format(e))

print("after badness")
