# Processes
# Imagine three completely separate restaurants.
# Restaurant A
# Restaurant B
# Restaurant C
# Each has:
# - Own kitchen
# - Own workers
# - Own ingredients
# They don't share anything.
# Very powerful.
# Uses more memory.


# 🔥 One Rule You'll Remember
# Ask yourself one question:
# If the CPU is doing heavy work:
# Image processing
# AI
# Math
# Encryption
# Compression
# → Multiprocessing


# Multiprocessing

from multiprocessing import Process
import time


def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")


if __name__ == "__main__":

    p = Process(target=worker)

    p.start()

    print("Main process")

    p.join()

    print("Program finished")


# Output:
# Main process
# Worker started
# Worker finished
# Program finished
#
# Explanation:
# p.start() starts the new process.
# p.join() makes the main process wait
# until the worker process finishes.
# After the worker process is completed,
# the program continues to the next lines of code.


# Comparison:
#
# | Feature             | Processes         | Threads                        | Async                            |
# | ------------------- | ----------------- | ------------------------------ | -------------------------------- |
# | Workers             | Multiple programs | Multiple threads               | One thread                       |
# | Memory              | Separate          | Shared                         | Shared                           |
# | Best for            | CPU-bound work    | Mixed/I/O work                 | I/O-bound work                   |
# | Runs simultaneously | Yes               | Often (with caveats in Python) | No, cooperatively switches tasks |
# | More memory         | Yes               | No                             | Very little                      |


# Difference between Threading and Async:
# Both are useful for I/O-bound tasks.
# Threading creates multiple threads
# that can run different tasks separately
# while sharing the same process memory.
#
# Async uses one thread and cooperatively switches
# between tasks when one task is waiting.
#
# When an async task is waiting for something like
# a network request, database response, or file operation,
# the event loop can run another task
# until the previous task is ready to continue.


# Multiprocessing Project → Number Calculator ⭐
from multiprocessing import Process
import time


def calculate(name):
    print(name, "started")

    total = 0

    for i in range(10000000):
        total += i

    print(name, "finished")


if __name__ == "__main__":

    p1 = Process(target=calculate, args=("Task 1",))
    p2 = Process(target=calculate, args=("Task 2",))


    p1.start()
    p2.start()


    p1.join()
    p2.join()


    print("Done")