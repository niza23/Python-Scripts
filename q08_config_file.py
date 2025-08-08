#!/usr/bin/env python3
"""
Q08: Config File

Task:
Read values from a configuration file using Python's `configparser` module.

Steps:
1. Load a config file
2. Access values from a specific section
3. Print the values

#config.ini:
[database]
user = admin
password = secret123

"""
# ==== Your Python code below ====

import configparser

config = configparser.ConfigParser()
config.read('config.ini') #reads the file

user = config['database']['user']
password = config['database']['password']

print(f"User: {user}")
print(f"Password: {password}")
