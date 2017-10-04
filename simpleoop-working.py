#!/usr/bin/env python3

# simple fibonacci series
# the sum of two elements defines the next set
# class = definition to create object (instance of class, blueprint)
class Fibonacci():
    # self = 1st arg, reference to object (in this case, 'f')
    # def __init__ = constructor
    # a, b = variables (in this case, '0, 1')
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')
