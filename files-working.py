#!/usr/bin/env python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    # writing normal files
    infile = open('lines-working.txt', 'r')
    outfile = open('new-writing-normal-working.txt', 'w')
    for line in infile:
        # print each line to outfile
        print(line, file = outfile, end = '')
    print('Done.')

    # writing big files
    buffersize = 50000 # set above to original file bytes
    infile = open('bigfile-working.txt', 'r')
    outfile = open('new-writing-big-working.txt', 'w')
    buffer = infile.read(buffersize) # read not line-by-line but bigger chunks
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '') # count num of chunks
        buffer = infile.read(buffersize)
    print()
    print('Done.')

    # reading/writing binary files (such as .jpg)
    buffersize = 50000 # set above to original file bytes
    infile = open('olives-working.jpg', 'rb')
    outfile = open('new-writing-binary-working.jpg', 'wb')
    buffer = infile.read(buffersize) # read not line-by-line but bigger chunks
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '') # count num of chunks
        buffer = infile.read(buffersize)
    print()
    print('Done.')

if __name__ == "__main__": main()
