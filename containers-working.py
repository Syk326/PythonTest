#!/usr/bin/env python3
# containers.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print('This is the containers.py file.')

    # use immutable tuples when you can, unless change is required -> list
    # tuples use ',' operator, not '()'
    t = (1,) # initialize with 1 element
    print(type(t))
    t = tuple(range(25)) # initialize with 0-24
    print(t)
    # t[10] = 42 -> NOPE. Immutable
    print(10 in t) # True
    print(50 in t) # False
    print(50 not in t) # True
    print(t.count(5)) # how many 5s?
    print(t.index(5)) # what index is 5?

    # lists
    x = list(range(25)) # initialize with 0-24
    print(x)
    x[10] = 42 # YEP.
    print(x)
    x.remove(12) # value 12
    print(x)
    del x[12] # index 12
    print(x)
    print(x.pop(12)) # gives index 12 and removes, default = last
    print(x)
    x.extend(range(20)) # appends another 0-19
    print(x)
    x.insert(0, 20) # insert value 20 at index 0
    print(x)

    # dictionaries
    d = dict(one = 1, two = 2, three = 3)
    print(d)
    x = dict(four = 4, five = 5, six = 6)
    print(x)
    d = dict(one = 1, two = 2, three = 3, **x) # combine above
    print(d)
    print('four' in x) # True
    print('three' in x) # False
    del x['four']
    print(x)
    print(x.pop('five')) # gives value at 'five' and removes
    print(x)

    for k in d: print(k) # iterate dict keys
    for k,v in d.items(): print(k, v) # iterate dict with values

    # bytes/bytearrays = tuples/lists with bytes -> convert strings!
    # operates on mutable bytearray
    fin = open('utf8-working.txt', 'r', encoding = 'utf_8')
    fout = open('utf8-working.html', 'w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else:
                outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print('Done.')

if __name__ == "__main__": main()
