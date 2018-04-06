#!/usr/bin/env python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('this is the switch.py file')

    # Equivalent to case/switch statements
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    # Find value for specific key
    v = 'three'
    print(choices[v])

    # When you want a 'default'
    x = 'seven'
    print(choices.get(x, 'other'))

if __name__ == "__main__": main()
