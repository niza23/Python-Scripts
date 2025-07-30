#!/usr/bin/env python3
"""
Q03: Env Variables

Task:
Access and print the value of any environment variable using Python.
Prompt the user to enter the variable name, then fetch and display its value.

Note:
If the environment variable is not set, `os.getenv()` will return `None`.

Steps:
1. Take the name of the environment variable as user input
2. Use `os.getenv()` to retrieve its value
3. Print the value or an appropriate message if it’s not set
"""

# ==== Your Python code below ====

import os

env_var = input("Enter the name of the environment variable (case-sensitive): ")

value = os.getenv(env_var)

if value is None:
    print(f"Environment variable '{env_var}' is not set.")
else:
    print(f"Value of '{env_var}': {value}")
