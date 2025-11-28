# 1. Initialize the logging configuration to capture timestamped messages.
import logging

# Setup logger
logging.basicConfig(
    filename='Process.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

logging.info("Logging initialized successfully!")


logging.info("Process started.")        

# 2. Define a function that simulates a process task
import time
import logging

# Dummy function to simulate a task
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)  # Simulate task delay
    logging.info(f"{task_name} ended")

# 3. Create at least two processes and start them concurrently.
import multiprocessing

if __name__ == '__main__':
    print("System Starting...")

    # Create processes
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))

    # Start processes
    p1.start()
    p2.start()

    # Optional: Wait for both to finish
    p1.join()
    p2.join()

    print("All processes completed.")


# 4.Ensure proper termination and verify logs
    p1.join()
    p2.join()
    print("System Shutdown.")




