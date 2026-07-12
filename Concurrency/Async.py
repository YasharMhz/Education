
# Async
# One chef.
# Start pasta
# ↓
# Water boiling?
# ↓
# No
# ↓
# Start sauce
# ↓
# Sauce cooking?
# ↓
# No
# ↓
# Cut vegetables
# ↓
# Water ready
# ↓
# Continue pasta
# Only ONE chef.
# He never wastes time waiting.


# 🔥 One Rule You'll Remember
# Ask yourself one question:
# "Is my program waiting, or is my CPU working hard?"
# If it's waiting:
# Network?
# Database?
# API?
# Files?
# → Async


import time

print("Start")

time.sleep(3)

print("Finished")


import asyncio


async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("World")


asyncio.run(hello())


# Difference between time.sleep() and await asyncio.sleep():
#
# time.sleep() blocks the entire program and stops the execution
# until the waiting time is finished.
#
# However, when we use await asyncio.sleep(),
# the program enters a waiting state and can continue running
# other tasks. When the waiting time is finished,
# it comes back and continues from where it stopped.


import asyncio


async def task1():
    print("A")

    await asyncio.sleep(5)

    print("B")


async def task2():
    print("C")

    await asyncio.sleep(1)

    print("D")


async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())


# Output: A C D B
#
# Explanation:
#
# In task1, "A" is printed immediately.
# Then the task waits for 5 seconds because of asyncio.sleep().
# While task1 is waiting, asyncio moves to task2.
# "C" is printed immediately.
# Task2 waits for 1 second, then "D" is printed.
# After that, task1 still needs 4 more seconds,
# so finally "B" is printed.


# Async Project → Async Task Manager ⭐
# This project demonstrates how asyncio can handle multiple waiting tasks concurrently.
import asyncio


async def send_email():
    print("Sending email...")
    await asyncio.sleep(3)
    print("Email sent")


async def save_data():
    print("Saving data...")
    await asyncio.sleep(2)
    print("Data saved")


async def main():
    await asyncio.gather(
        send_email(),
        save_data()
    )


asyncio.run(main())

