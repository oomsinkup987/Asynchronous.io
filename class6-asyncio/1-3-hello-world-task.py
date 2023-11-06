import asyncio
import time 

async def print_after(message, delay):
  #print a message after the sepcified delay (in seconds)
    await asyncio.sleep(delay)
    print(f"{time.ctime()} - {message} ")

async def main():
    #Start coroutine twice (Hopefully they stary!)
    first_awaitabel = asyncio.create_task(print_after("world!", 2))
    second_awaitbel = asyncio.create_task(print_after("world!", 1))
    #Wait for coroutines to finish
    await first_awaitabel
    await second_awaitbel

asyncio.run(main())