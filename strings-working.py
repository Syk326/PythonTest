#!/usr/bin/env python3
# strings.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # both are str objects, does the same thing
    s = 'this is a string'
    print(s.upper())
    print('this is a string'.upper())

    # s doesn't change, str = immutable
    print(s.capitalize())

    # other str functions
    title = s.title()
    print(title)
    print(title.swapcase())
    print(s.find('is')) # finds the index
    print(s.replace('this', 'that'))
    print('     this is a string     '.strip()) # removes beginning/end space
    print('     this is a string     '.rstrip()) # removes end space only
    print('this is a string\n'.rstrip('\n')) # removes end value

    # "is" functions
    no_space = 'thisisastring'
    print(no_space.isalnum()) # alphanumeric chars?
    print(no_space.isalpha()) # alpha chars?
    print(no_space.isdigit()) # digit chars?
    print(no_space.isprintable()) # printable chars?

    a, b = 5, 42
    t = 'this is {}'
    print(t.format(a)) # format after the fact
    print('this is {1}, that is {0}'.format(a, b)) # insert by index
    print('this is {bob}, that is {fred}'.format(bob=a, fred=b)) # any variable name
    d = dict(bob=a, fred=b)
    print('this is {bob}, that is {fred}'.format(**d)) # format with dict variable
    print(s.split()) # split string by spaces
    print(s.split('i')) # split string by 'i'
    words = s.split()
    print(':'.join(words)) # join split string by ':'

if __name__ == "__main__": main()
