#!/usr/bin/env python3

a, b = 0, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

# readable version of a < b ? "foo" : "bar" from other languages
print("foo" if a < b else "bar")
