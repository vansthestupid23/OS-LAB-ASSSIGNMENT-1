# Write a Python program that creates N child processes using os.fork(). Each child prints:
# - Its PID
# - Its Parent PID
# - A custom message
# The parent should wait for all children using os.wait().

import os

def create_children(n):
    print(f"Parent process started with PID: {os.getpid()}\n")
    for i in range(n):
        pid = os.fork()

        if pid == 0:
            print(f"Child {i+1}:")
            print(f"  PID: {os.getpid()}")
            print(f"  Parent PID: {os.getppid()}")
            print(f"  Message: Hello, I am child process number {i+1}\n")
            os._exit(0) 
        else:
            continue
    for _ in range(n):
        os.wait()
    print("\nAll child processes have finished.")

if __name__ == "__main__":
    N = int(input("Enter number of child processes to create: "))
    create_children(N)


# Zombie: Fork a child and skip wait() in the parent.
# Orphan: Parent exits before the child finishes.
# Use ps -el | grep defunct to identify zombies.

import time

print(f"Parent PID: {os.getpid()}")

pid = os.fork()

if pid == 0:
    print(f"Child PID: {os.getpid()} (will exit soon)")
    time.sleep(1)
    print("Child exiting...")
    os._exit(0)
else:
    print(f"Parent continues without waiting for child (PID: {pid})")
    time.sleep(10) 
    print("Parent exiting...")


# Take a PID as input. Read and print:
# - Process name, state, memory usage from /proc/[pid]/status
# - Executable path from /proc/[pid]/exe
# - Open file descriptors from /proc/[pid]/fd

def read_process_info(pid):
    status_path = f"/proc/{pid}/status"
    exe_path = f"/proc/{pid}/exe"
    fd_path = f"/proc/{pid}/fd"
    try:
        with open(status_path, 'r') as f:
            lines = f.readlines()
        process_info = {}
        for line in lines:
            if line.startswith(("Name:", "State:", "VmRSS:")):
                key, value = line.split(":", 1)
                process_info[key.strip()] = value.strip()

        print("\n--- Process Information ---")
        print(f"Name: {process_info.get('Name', 'N/A')}")
        print(f"State: {process_info.get('State', 'N/A')}")
        print(f"Memory Usage: {process_info.get('VmRSS', 'N/A')}")
    except FileNotFoundError:
        print(f"❌ Process with PID {pid} does not exist.")
        return
    try:
        exe_real_path = os.readlink(exe_path)
        print(f"Executable Path: {exe_real_path}")
    except Exception as e:
        print(f"Could not read executable path: {e}")
    try:
        print("\n--- Open File Descriptors ---")
        for fd in os.listdir(fd_path):
            fd_full_path = os.path.join(fd_path, fd)
            try:
                target = os.readlink(fd_full_path)
                print(f"FD {fd}: {target}")
            except OSError:
                print(f"FD {fd}: [Unavailable]")
    except FileNotFoundError:
        print("No open file descriptors found.")

if __name__ == "__main__":
    pid = input("Enter PID: ").strip()
    if pid.isdigit():
        read_process_info(pid)
    else:
        print("Please enter a valid numeric PID.")


# Create multiple CPU-intensive child processes. Assign different nice() values. Observe and log execution order to show scheduler impact.

import os
import time

def cpu_task(task_id, nice_value):
    os.nice(nice_value)
    start = time.time()
    print(f"[Child {task_id}] PID={os.getpid()}, Nice={nice_value}, Started at {time.strftime('%H:%M:%S')}")
    total = 0
    for i in range(10**7):
        total += i % 5

    end = time.time()
    print(f"[Child {task_id}] PID={os.getpid()} Finished in {end - start:.2f}s | Nice={nice_value}")

def main():
    num_children = 3
    nice_values = [-5, 0, 10]

    print(f"Parent PID: {os.getpid()}\nCreating {num_children} child processes...\n")

    for i in range(num_children):
        pid = os.fork()
        if pid == 0:
            cpu_task(i+1, nice_values[i])
            os._exit(0)

    # Parent waits for all children
    for _ in range(num_children):
        os.wait()

    print("\nAll children finished execution.")

if __name__ == "__main__":
    main()
