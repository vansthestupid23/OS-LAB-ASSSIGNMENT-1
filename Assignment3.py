# 1. Write a Python program to simulate Priority and Round Robin scheduling algorithms. Compute average waiting and turnaround times.

# # -----------------------------
# # PRIORITY SCHEDULING (Non-Preemptive)
# # -----------------------------
# def priority_scheduling(processes):
#     # processes = [(pid, burst_time, priority), ...]

#     # Sort by priority
#     processes.sort(key=lambda x: x[2])

#     n = len(processes)
#     waiting_time = [0] * n
#     turnaround_time = [0] * n

#     # Waiting time
#     for i in range(1, n):
#         waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

#     # Turnaround time
#     for i in range(n):
#         turnaround_time[i] = waiting_time[i] + processes[i][1]

#     avg_wait = sum(waiting_time) / n
#     avg_tat = sum(turnaround_time) / n

#     print("\n--- Priority Scheduling ---")
#     print("PID\tBT\tPR\tWT\tTAT")
#     for i, p in enumerate(processes):
#         print(f"{p[0]}\t{p[1]}\t{p[2]}\t{waiting_time[i]}\t{turnaround_time[i]}")

#     print(f"\nAverage Waiting Time: {avg_wait:.2f}")
#     print(f"Average Turnaround Time: {avg_tat:.2f}")


# # -----------------------------
# # ROUND ROBIN SCHEDULING
# # -----------------------------
# def round_robin(processes, quantum):
#     # processes = [(pid, burst_time), ...]

#     n = len(processes)
#     remaining_bt = [p[1] for p in processes]
#     waiting_time = [0] * n
#     turnaround_time = [0] * n

#     time = 0

#     while True:
#         done = True

#         for i in range(n):
#             if remaining_bt[i] > 0:
#                 done = False

#                 if remaining_bt[i] > quantum:
#                     time += quantum
#                     remaining_bt[i] -= quantum
#                 else:
#                     time += remaining_bt[i]
#                     waiting_time[i] = time - processes[i][1]
#                     remaining_bt[i] = 0

#         if done:
#             break

#     # Turnaround time = BT + WT
#     for i in range(n):
#         turnaround_time[i] = processes[i][1] + waiting_time[i]

#     avg_wait = sum(waiting_time) / n
#     avg_tat = sum(turnaround_time) / n

#     print("\n--- Round Robin Scheduling ---")
#     print("PID\tBT\tWT\tTAT")
#     for i, p in enumerate(processes):
#         print(f"{p[0]}\t{p[1]}\t{waiting_time[i]}\t{turnaround_time[i]}")

#     print(f"\nAverage Waiting Time: {avg_wait:.2f}")
#     print(f"Average Turnaround Time: {avg_tat:.2f}")


# if __name__ == "__main__":
#     print("\n=== PRIORITY SCHEDULING INPUT ===")
#     n1 = int(input("Enter number of processes: "))

#     processes_priority = []
#     for i in range(n1):
#         pid = input(f"Enter Process ID for P{i+1}: ")
#         bt = int(input(f"Enter Burst Time for {pid}: "))
#         pr = int(input(f"Enter Priority for {pid}: "))
#         processes_priority.append((pid, bt, pr))

#     # Run Priority Scheduling
#     priority_scheduling(processes_priority)

#     print("\n=== ROUND ROBIN SCHEDULING INPUT ===")
#     n2 = int(input("Enter number of processes: "))

#     processes_rr = []
#     for i in range(n2):
#         pid = input(f"Enter Process ID for P{i+1}: ")
#         bt = int(input(f"Enter Burst Time for {pid}: "))
#         processes_rr.append((pid, bt))

#     quantum = int(input("Enter Time Quantum: "))

#     # Run Round Robin
#     round_robin(processes_rr, quantum)

# 2. Write a Python program to simulate indexed file allocation strategy.

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks

n = int(input("Enter number of files: "))

for i in range(n):
    start = int(input(f"\nEnter starting block for File {i+1}: "))
    length = int(input(f"Enter length of file {i+1}: "))

    allocated = True

    # Check availability
    for j in range(start, start + length):
        if j >= total_blocks or block_status[j] == 1:
            allocated = False
            break

    # Allocate blocks
    if allocated:
        for j in range(start, start + length):
            block_status[j] = 1
        print(f"File {i+1} allocated from block {start} to {start + length - 1}")
    else:
        print(f" File {i+1} cannot be allocated.")

# 3.Write a Python program to simulate indexed file allocation strategy.
# Task 4: Indexed File Allocation

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks

n = int(input("Enter number of files: "))

for i in range(n):
    index = int(input(f"\nEnter index block for File {i+1}: "))

    if index >= total_blocks or block_status[index] == 1:
        print("❌ Index block already allocated or invalid.")
        continue

    count = int(input("Enter number of data blocks: "))
    data_blocks = list(map(int, input("Enter block numbers: ").split()))

    if len(data_blocks) != count:
        print("❌ Invalid number of data blocks.")
        continue

    if any(blk >= total_blocks or block_status[blk] == 1 for blk in data_blocks):
        print("❌ One or more blocks already allocated.")
        continue

    # Allocate index + data blocks
    block_status[index] = 1
    for blk in data_blocks:
        block_status[blk] = 1

    print(f"✅ File {i+1} allocated successfully.")
    print(f"Index Block → {index}")
    print(f"Data Blocks → {data_blocks}")

# 4. Simulate Worst-fit, Best-fit, and First-fit memory allocation strategies.

# Task 5: Contiguous Memory Allocation

def allocate_memory(strategy):
    print(f"\n--- {strategy.upper()} FIT ALLOCATION ---")

    partitions = list(map(int, input("Enter partition sizes: ").split()))
    processes = list(map(int, input("Enter process sizes: ").split()))
    allocation = [-1] * len(processes)

    for i, psize in enumerate(processes):
        idx = -1

        if strategy == "first":
            for j, part in enumerate(partitions):
                if part >= psize:
                    idx = j
                    break

        elif strategy == "best":
            best = float("inf")
            for j, part in enumerate(partitions):
                if part >= psize and part < best:
                    best = part
                    idx = j

        elif strategy == "worst":
            worst = -1
            for j, part in enumerate(partitions):
                if part >= psize and part > worst:
                    worst = part
                    idx = j

        if idx != -1:
            allocation[i] = idx
            partitions[idx] -= psize

    # Print results
    for i, a in enumerate(allocation):
        if a != -1:
            print(f"Process {i+1} allocated in Partition {a+1}")
        else:
            print(f"Process {i+1} cannot be allocated")

# Calling all three
allocate_memory("first")
allocate_memory("best")
allocate_memory("worst")




