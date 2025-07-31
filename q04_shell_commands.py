#!/usr/bin/env python3
"""
Q04: Shell Commands

Task:
Execute a shell command from within a Python script using the `subprocess` module.
In this example, run the `ls -l` command to list directory contents in long format,
capture the output, and print it.

Steps:
1. Use `subprocess.run()` to execute the shell command
2. Set `capture_output=True` and `text=True` to capture readable output
3. Print the standard output to the console
"""

# ==== Your Python code below ====

import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

#print(f"it shows the complete process '{result}'")  

print(result.stdout)

#Use result.stdout to get what the command actually printed.

#Use result.stderr if you want to capture error messages.

#Use result.returncode to check if the command succeeded.
