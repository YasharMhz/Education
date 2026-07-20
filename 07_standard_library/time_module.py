
# time_module.py

import time


# -----------------------------
# 1. Get current timestamp
# -----------------------------

current_time = time.time()

print("Current timestamp:", current_time)


# time.time()
# returns the number of seconds since January 1, 1970
# (Unix Epoch)


# -----------------------------
# 2. Sleep function
# -----------------------------

print("Start")

time.sleep(3)

print("End")


# sleep()
# pauses the execution of the program
# for a specific number of seconds


# -----------------------------
# 3. Measure execution time
# -----------------------------

start_time = time.time()


total = 0

for i in range(1_000_000):
    total += i


end_time = time.time()


execution_time = end_time - start_time


print("Execution time:", execution_time)


# We can use time.time()
# to measure how long a task takes


# -----------------------------
# 4. Create a simple timer
# -----------------------------

seconds = 5

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1


print("Time is finished!")
