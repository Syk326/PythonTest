#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the variables.py file.")

    # everything is object, all have id (immutable), class (immutable), value (mutable depending on class)
    x = 42
    print(id(x))
    print(type(x))
    print(x)

    y = 42
    print(x==y) # compare values
    print(x is y) # compare id

    a = dict(c = 42)
    b = dict(c = 42)
    print(a == b) # True
    print(a is b) # False (id is diff)

    # raw string
    s = r'This is a\nstring'
    print(s) # prints including \n

    # multi-line string
    t = '''\
    this is a string
    line after line
    of text and more
    text.
    '''
    print(t) # the '\' gets rid of blank line at top

    # sort dictionary
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    for k in sorted(d.keys()): # sorted alphabetically
        print(k, d[k])
    # faster way to create dictionary
    i = dict(
        one = 1, two = 2, three = 3, four = 4, five = 5
    )
    i['seven'] = 7
    print(i)

if __name__ == "__main__": main()
