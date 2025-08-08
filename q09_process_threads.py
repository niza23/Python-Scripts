#!/usr/bin/env python3
"""
Q09: Process Threads

Task:
Run a function in a separate thread using Python's `threading` module. This allows parallel execution of tasks without blocking the main thread.

Steps:
1. Define a function that prints numbers with a delay
2. Start a new thread that runs the function
3. Let the main thread continue running independently

***What's Happening Behind the Scenes:****
threading.Thread(...) creates a new thread instance, but does not start it yet.

The target parameter tells Python:
➝ "When the thread starts, run this function."

thread.start() triggers the parallel execution of that function.

Meanwhile, your main program keeps running — it doesn't wait for the thread to finish unless you use thread.join().
"""

# ==== Your Python code below ====

import threading
import time

def print_num():
    for i in range(5):
        print(i)
        time.sleep(1)  # simulate work by waiting 1 second

# Create a Thread object that will run the function `print_num` in parallel
# `target=print_num` tells the thread *what function* to execute
thread = threading.Thread(target=print_num)

# Start the thread — this begins execution of `print_num()` in the background
# It runs independently of the main thread, so the main program continues immediately
thread.start()


# Main thread does not wait
print("main thread continues")
