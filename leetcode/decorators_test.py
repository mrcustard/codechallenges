#!/usr/bin/env python3

# example of how to use decorators, which are just wrappers around functions

def my_decorator(func):
    def wrapper():
        print("Somehting is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper



@my_decorator
def say_hello():
    print("Hello!")


say_hello()