#!/usr/bin/env python3

"""
Q01: Read Write File

Task:
Create a file named 'example.txt', write the string "this is sample file" into it,
then read the content and print it to stdout.

Steps:
1. Open the file in write mode and write a string to it, use "with": It ensures the file is automatically closed when the block ends, even if there’s an error
2. Close and reopen the file in read mode
3. Read the content and print it
"""

# ==== Your Python code below ====

# Writing to a file
with open('example.txt', 'w') as f:
    f.write("this is sample file")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
