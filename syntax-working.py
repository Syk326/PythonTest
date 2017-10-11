#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
# Always use comments as guideline, not gospel

def main():
    print("This is the syntax.py file.")
    tacos()

    # create object from class, which is definition
    fried = Egg() # fried by default
    scrambled = Egg('scrambled') # can change arguments
    print(fried.whatKind())
    print(scrambled.whatKind())

# Defined function AFTER calling it, but will still work because of "def main()" above and the line at the bottom
def tacos():
    print("tacos")
    for i in range(10):
        print(i, end = ' ') # adds space to end on one line
    print('\n')

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind

# runs at the end
# if function is only 1 line, can add after ":" without spacing
if __name__ == "__main__": main()
