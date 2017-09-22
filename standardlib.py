# Python Standard Library: import modules @ top
import math # math module
# from module_name import object_name <- import individual function
from random import randrange
from datetime import datetime
from collections import defaultdict, namedtuple # import multiple objects
from csv import reader as csv # rename the module
import os.path # submodule
# DON'T: from module_name import * <- may overwrite your code accidentally, just do: import module_name
# DON'T: import os.path.isdir <- won't work to import function

# third-party packages: large programs may depend on dozens
# import pytz <- 3rd party library
# FIRST: pip3 install pytz <- pip comes with python3
"""
share large programs with requirements.txt:
Lists out a project's dependencies, each line has package name & optional ver. #
pip3 install -r requirements.txt <- install ALL dependencies

utc = pytz.utc # coordinated universal time
ist = pytz.timezone('Asia/Kalkata') # Indian Standard Time
now = datetime.datetime.now(tz=utc) # time in UTC
ist_now = now.astimezone(ist) # time in IST
"""

# use "random" package from standard library to complete
word_file = "words.txt"
word_list = []
#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)
def generate_password():
    # Return a string consisting of three random words concatenated together without spaces
    rand_string = ""
    for i in range(3):
        rand_num = randrange(len(word_list))
        rand_string += word_list[rand_num]
    return rand_string
print(generate_password())
