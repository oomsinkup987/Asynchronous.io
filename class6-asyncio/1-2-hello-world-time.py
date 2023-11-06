import asyncio
import time 

async def example(message):
    print("f{time.ctime} - start of :" , message)
    await asyncio.sleep(1)
    print("f{time.ctime} - end of :" , message)

async def main():
    #Start coroutine twice (Hopefully they stary!)
    first_awaitabel = example("First call")
    second_awaitbel = example("Second call")
    #Wait for coroutines to finish
    await first_awaitabel
    await second_awaitbel

asyncio.run(main())
