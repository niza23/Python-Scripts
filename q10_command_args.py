#!/usr/bin/env python3
"""
Q10: Command Args

Task:
Write a Python script that accepts command-line arguments, processes them, 
and prints them back in a formatted way. 
If no arguments are provided, display usage instructions.

Steps:
1. Import the sys module to read command-line arguments.
2. Check if arguments are provided.
3. Display the arguments in a readable format.

Tags: #python #devops #scripting
"""

import sys

def main():
    # sys.argv[0] is the script name
    args = sys.argv[1:]
    
    if not args:
        print("Usage: python3 script.py <arg1> <arg2> ...")
        print("Example: python3 script.py hello world")
        sys.exit(1)

    print("Number of arguments:", len(args))
    print("Arguments list:", args)

    # Optional: formatted output
    for i, arg in enumerate(args, start=1):
        print(f"Arg {i}: {arg}")

if __name__ == "__main__":
    main()
