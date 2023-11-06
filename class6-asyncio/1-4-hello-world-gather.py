import asyncio
import time 

async def print_after(message, delay):
  #print a message after the sepcified delay (in seconds)
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message} ")

async def main():
   #Use asynico.gather to run two corountines concurrenyly
   await asyncio.gather(
       print_after("world!", 2),
       print_after("world!", 1),
   )

asyncio.run(main())