#!/usr/bin/env python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# decorators = functions that return other functions (modify how works)
class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    # used the follow decorators on functions
    @property
    def color(self):
        return self.properties.get('color', None)
    @color.setter
    def color(self, c):
        self.properties['color'] = c
    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    #donald = Duck(color = 'blue')
    #print(donald.get_property('color'))
    #OR:

    # under control of the object
    donald = Duck()
    donald.color = 'blue'
    print(donald.color)

if __name__ == "__main__": main()
