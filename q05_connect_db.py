#!/usr/bin/env python3
"""
Q05: Connect to DB

Task:
Demonstrate how to connect to a local SQLite3 database using Python.
This example creates a new SQLite database (if it doesn’t exist), creates a table,
inserts some sample data, and queries it.

Steps:
1. Connect to or create an SQLite3 database file
2. Create a table if it doesn't exist
3. Insert and fetch data using SQL queries
"""

# ==== Your Python code below ====

import sqlite3

# Step 1: Connect to a local database (creates file if it doesn't exist)
conn = sqlite3.connect('sample.db')

# Step 2: Create a cursor object to interact with the database
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Step 4: Insert sample data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alce@example.com"))

# Step 5: Query and print all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 6: Commit changes and close the connection
conn.commit()
conn.close()
