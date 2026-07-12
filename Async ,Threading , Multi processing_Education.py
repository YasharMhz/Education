#processes =
# Imagine three completely separate restaurants.
# Restaurant A
# Restaurant B
# Restaurant C
# Each has:
# own kitchen
# own workers
# own ingredients
# They don't share anything.
# Very powerful.
# More memory.

# Threads
# # One restaurant.
# # Three chefs.
# # Kitchen
# # Chef 1
# # Chef 2
# # Chef 3
# # They share the same kitchen.
# # Faster communication.
# # Need coordination.

# Async
# # One chef.
# # Start pasta
# # ↓
# # Water boiling?
# # ↓
# # No
# # ↓
# # Start sauce
# # ↓
# # Sauce cooking?
# # ↓
# # No
# # ↓
# # Cut vegetables
# # ↓
# # Water ready
# # ↓
# # Continue pasta
# # Only ONE chef.
# # He never wastes time waiting.

# | Feature             | Processes         | Threads                        | Async                            |
# | ------------------- | ----------------- | ------------------------------ | -------------------------------- |
# | Workers             | Multiple programs | Multiple threads               | One thread                       |
# | Memory              | Separate          | Shared                         | Shared                           |
# | Best for            | CPU-bound work    | Mixed/I/O work                 | I/O-bound work                   |
# | Runs simultaneously | Yes               | Often (with caveats in Python) | No, cooperatively switches tasks |
# | More memory         | Yes               | No                             | Very little                      |

# import time
#
# print("Start")
#
# time.sleep(3)
#
# print("Finished")
#
# import asyncio
#
# async def hello():
#     print("Hello")
#     await asyncio.sleep(2)
#     print("World")
#
# asyncio.run(hello())

#tafavote time.sleep() va await asyncio.sleep() = ine ke time.sleep() kole barname ro hamoonja negah midare ta karesh anjam beshe
#vali ba estefade az await asyncio.sleep() vaghti mire roo waiting mire be khat haye bad vaghti zamane code ma tamom mishe barmigarde be code asli
#daghighan hamin shekl dar code paeen moshakhase

# import asyncio
# #async = yani momkene toye in ghesmat ye wait dashte bashim
# async def task1():
#     print("A")
# #await = yani agar in ghesmta raft roo halate waiting boro ghesmate bad ta man az waiting dar biam
# #asyncio.sleep(5) = yani 5 sanie sabr kon ta man karam tamom beshe bad print("B") ro anjam bede
#     await asyncio.sleep(5)
#     print("B")
#
# async def task2():
#     print("C")
#     await asyncio.sleep(1)
#     print("D")
#
# #main = yek fuction ke ba estefade az oon task1 va task 2ro baham run kardim
# async def main():
# #asyncio.gather = yani task 1 va task 2 ro hamzaman run kon
#     await asyncio.gather(
#         task1(),
#         task2()
#     )
#asyncio.run(main()) = yani function main ro run kon
# asyncio.run(main())
#output = A C D B chon dar task1 sari A chap mishe mire be khate bad ke bayad 5sec sabr kone bad ejra beshe
#in ghesmate mire roo halate waiting baraye hamin mirim soraghe task2 sari C ro chap mikonim bad mirim khate bad
# dar inja bayad 1sec sabr konim ke in khat ejra beshe 1sec sabr mikonim D print mishe va bad 4sec dige sabr
#mikonim ke B ham chap beshe


# threading
import threading
import time

def task(name):
    print(name, "started")
    time.sleep(2)
    print(name, "finished")

#target=task = esme function
# args=("A",) = vorodi function
t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

#t1.start() = calle functioni ke be t1 vasle(target) ba voroodi ke dadim behesh(args)
t1.start()
t2.start()

# 🔥 One Rule You'll Remember
#
# Ask yourself one question:
#
# "Is my program waiting, or is my CPU working hard?"
#
# If it's waiting:
#
# Network?
# Database?
# API?
# Files?
#
# → Async
#
# If the CPU is doing heavy work:
#
# Image processing
# AI
# Math
# Encryption
# Compression
#
# → Multiprocessing
#
# If you're using blocking libraries or need background tasks (like a GUI staying responsive):
#
# → Threading

#Multiprocessing

# from multiprocessing import Process
# import time
#
# def worker():
#     print("Worker started")
#     time.sleep(2)
#     print("Worker finished")
#
# #code zir baraye nagereftane error estefade mishe
# if __name__ == "__main__":
#     p = Process(target=worker)
#
# #p.start() = yani p ro run kon
#     p.start()
#
#     print("Main process")
#
# #p.join() = yani ta zamani ke p karesh tamoom nashode stop kon current program ro
#     p.join()

    # print("Program finished")
#output = Main process
# Worker started
# Worker finished
# Program finished
#chon p.start faghat run mikone va p.join mige current program ro stop kon ta zamani ke kare p camel tamoom beshe
#va bad be soraghe baghie cod boro

#tafavote threading va async =
#Bayad begi joftesho bara task haye io bound hastan vali threading miad ro ye core cpu chand bar on task ro run mikone
# ke az ham jodas vali async harja ke dige task mire ro halat wait me niaz be process kharej az code ma dare miad mire
# task baadi ro anjam mide ta ghabli dobare shoro beshe


