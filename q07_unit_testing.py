#!/usr/bin/env python3
"""
Q07: Unit Testing

Task:
Demonstrate how to write unit tests using Python’s built-in `unittest` module.
This example includes a simple function and a corresponding test case class.

Steps:
1. Define a function to test (e.g., `add`)
2. Create a class inheriting from `unittest.TestCase`
3. Write test methods using `assertEqual()` or other assertions
"""

# ==== Your Python code below ====

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
