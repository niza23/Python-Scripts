#!/usr/bin/env python3
"""
Q06: Decorators

Task:
Demonstrate how to create and use a simple decorator in Python.
This example wraps a function to add behavior before and after the original function call.

Steps:
1. Define a decorator function that takes another function as input
2. Add logic before and after calling the original function
3. Use the `@decorator_name` syntax to apply it to another function
"""

# ==== Your Python code below ====

def my_decorator(func):
    def wrapper():
        print("Before the call")
        func()
        print("After the call")
    return wrapper    

@my_decorator 
def say_hello():
    print("HELLO")

say_hello()
