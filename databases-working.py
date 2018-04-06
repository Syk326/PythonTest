#!/usr/bin/env python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# Databases, sqlite3 packaged with Python Standard Library
# https://docs.python.org/2/library/sqlite3.html
# Reliable, simple, self-contained, server-less, 0 config, fully transactional
# mangodb tends to be used more these days -> pip install pymongo, import pymongo
# https://api.mongodb.com/python/current/
import sqlite3

def main():
    print('This is the databases.py file')
    # creates the db
    db = sqlite3.connect('test.db')

    # use this to specify how rows will be returned from the cursor
    # comes out as row objects, not tuples
    db.row_factory = sqlite3.Row

    # populate the db
    db.execute('drop table if exists test')
    # the name of the table is 'test'
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
    # commits changes to db
    db.commit()
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        #print(row)
        print(dict(row)) # if row factory enabled
        print(row['t1'], row['i1']) # if row factory enabled

if __name__ == "__main__": main()
