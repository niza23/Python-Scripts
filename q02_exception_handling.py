#!/usr/bin/env python3
"""
Q02: Exception Handling

Task:
Demonstrate Python exception handling by attempting to divide a number by zero.
Catch the error using `try-except`, use `else` to handle success, and `finally`
to perform a clean-up action that runs regardless of an exception.

Steps:
1. Attempt division inside a `try` block
2. Handle ZeroDivisionError using `except`
3. Use `else` to print success message (not executed here)
4. Use `finally` to print "execution completed"
"""

# ==== Your Python code below ====

try:
    value = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division was successful")
finally:
    print("Execution completed")
