#!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re
# Regular Expressions: regex
# used to match patterns in text

def main():
    print("--TESTS FINDING LINES WITH LENORE/NEVERMORE--")
    fh = open('raven-working.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')

    print("--TESTS PRINTING ALL WORDS THAT MATCH--")
    fh = open('raven-working.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())

    print("--TESTS REPLACING MATCHING WORDS IN ENTIRE FILE--")
    fh = open('raven-working.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end = '')

    print("--TESTS PRINTING LINES WHERE WORD WAS REPLACED--")
    fh = open('raven-working.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end = '')

    print("--TESTS PRE-COMPILED SEARCH, INCLUDES LOWERCASE WORDS--")
    fh = open('raven-working.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end = '')

    print("--TESTS REPLACING IN PRE-COMPILED SEARCH--")
    fh = open('raven-working.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end = '')

if __name__ == "__main__": main()
