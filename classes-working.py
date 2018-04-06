#!/usr/bin/env python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

# super/parent class
class Animal:
    def talk(self): print('I have something to say')
    def walk(self): print("I'm walkin' here!")
    def clothes(self): print('I have nice clothes')

# inherits Animal
class Duck(Animal):
    # constructor, takes any keyword arg
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')
    def walk(self):
        # access function in parent class
        super().walk()
        print('Walks like a duck.')
    def fur(self):
        print('This duck be furless')
    def bark(self):
        print('The duck doesn\'t bark')

    # getters and setters, scalable
    # k = variable name
    # v = variable value
    def set_variable(self, k, v):
        self.variables[k] = v
    def get_variable(self, k):
        return self.variables.get(k, None)

# inherits Animal
class Dog(Animal):
    def quack(self):
        print('The dog doesn\'t quack')
    def walk(self):
        print('Walks like a dog')
    def fur(self):
        print('I have golden fur')
    def bark(self):
        print('Wooooof!')
    def clothes(self):
        print('I wear a golden fur coat')

def main():
    # set whatever variable you like
    donald = Duck(feet = 2)
    # call those object methods
    donald.quack()
    donald.walk()
    # not set
    print(donald.get_variable('color'))
    print(donald.get_variable('feet'))
    # stores object data in dictionary objects, lots of flexibility
    # use a lot of diff data, lot of flags and attributes, save to db, scale
    # CONTROL!!
    donald.set_variable('color', 'blue')
    # now has been set
    print(donald.get_variable('color'))
    spike = Dog()
    spike.clothes()

    # will run regardless of object type, as long as function is there
    for o in (donald, spike):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

    # see below
    in_the_forest(donald)
    in_the_pond(spike)

# takes any object not just dog, "duck-typing" (if walks & quacks like a duck)
def in_the_forest(dog):
    dog.bark()
    dog.fur()

# takes any object not just dog, "duck-typing" (if walks & quacks like a duck)
def in_the_pond(duck):
    duck.quack()
    duck.walk()

if __name__ == "__main__": main()
