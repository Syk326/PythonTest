#!/usr/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    print("This is the ops.py file.")

    # Equivalent of (5 // 3, 5 % 3)
    divmod(5, 3)
    # = 1 remainder 2, or: (1, 2)

    True and True #boolean
    True & True #bitwise

    list = []
    list[:] = range(100) # list = [0, 1, 2... 98, 99], value = index
    print(list)
    print(list[27:42:3]) # prints every 3rd value in the range
    list[27:42:3] = (99,99,99,99,99) #replaces those values with 99
    print(list)

if __name__ == "__main__": main()
