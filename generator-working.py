#!/usr/bin/env python3
# generator function creates iterator

# utility function
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

# generator
def primes(n = 1):
   while(True):
       # True/False, if True: return n <- ONLY 1ST EXECUTION
       # returns iterator object suitable for use in for loop
       if isprime(n): yield n
       n += 1

# uses iterator object in primes()
for n in primes():
    if n > 100: break
    print(n)
