# Write a Python script to execute multiple .py files sequentially, mimicking batch processing.

import os

# List of Python files to execute
files = ["Assignment1.py", "Assignment2.py", "Assignment3.py", "Assignment4.py"]

for file in files:
    print(f"\nExecuting {file}")
    os.system(f"python {file}")
    print(f"Finished {file}")

print("\nAll files executed successfully.")

# 2Simulate system startup using Python by creating multiple processes and logging their start and end into a log file.

import os
import time
import logging

# Configure logging
logging.basicConfig(filename='system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# List of processes to simulate
processes = [
    "Process A",
    "Process B",
    "Process C",
    "Process D",
    "Process E"
]

# Simulate startup
logging.info("System startup sequence initiated...")

for process in processes:
    logging.info(f"Starting {process}")
    time.sleep(2)  # Simulate process startup time
    logging.info(f"Finished {process}")

logging.info("System startup sequence completed.")

print("System startup simulation completed. Check 'system.log' for details.")
