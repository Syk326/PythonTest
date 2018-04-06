#!/usr/bin/env python3
# iterators.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # Fibonacci while loop
    a, b = 0, 1
    while b < 150:
        print(b, end = '') # prevents adding new line
        a, b = b, a + b
    print("")
    # how common are loops? for > while

    fh = open('lines-working.txt')
    for line in fh.readlines():
        print(line) # prints all lines
    fh.close()

    # Enumerate iterators
    # index and line variables can be named anything
    lh = open('lines-working.txt')
    for index, line in enumerate(lh.readlines()):
        print(index, line, end = '') # prevents adding new blank line
    lh.close()

    # can do with strings too
    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))

if __name__ == "__main__": main()
