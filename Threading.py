# Threads
# One restaurant.
# Three chefs.
# Kitchen
# Chef 1
# Chef 2
# Chef 3
# They share the same kitchen.
# Faster communication.
# Need coordination.


# 🔥 One Rule You'll Remember
# Ask yourself one question:
# If you're using blocking libraries
# or need background tasks
# (like a GUI staying responsive):
# → Threading


import threading
import time


def task(name):
    print(name, "started")
    time.sleep(2)
    print(name, "finished")


t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))


t1.start()
t2.start()
t1.join()
t2.join()

print("Done")

# join() makes the main thread wait until
# the worker threads finish their tasks.


# Explanation:
# threading.Thread creates a new thread.
# target=task means the function that the thread will execute.
# args=("A",) passes the input value to the function.
# t1.start() starts the thread and runs the task function.
# t2.start() starts another thread at the same time.


# Threading Project → Restaurant Order System ⭐
import threading
import time


def cook(order):
    print(order, "started")

    time.sleep(3)

    print(order, "finished")


t1 = threading.Thread(target=cook, args=("Pizza",))
t2 = threading.Thread(target=cook, args=("Burger",))
t3 = threading.Thread(target=cook, args=("Pasta",))


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("All orders finished")