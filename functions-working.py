#!/usr/bin/env python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1, 2, 3, 42, 43, 45, one = 1, two = 2, four = 4)

# *args = args, tuple default
# **kwargs = keyword args, dict default
def testfunc(this, that, other, *args, **kwargs):
    print(this, that, other, args, kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()
