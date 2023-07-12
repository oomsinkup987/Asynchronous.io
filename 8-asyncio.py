#example of running a blocking io-bound task in asyncio
import asyncio
import time

#a blocking io-bound task
def blocking_task():
    #report a message
    print(f'{time.ctime()} Task starting...')
    time.sleep(2)
    #report message
    print(f'{time.ctime()} Task done')

#main coroutine
async def main():
    #report a message 
    print(f'{time.ctime()} Main running the blocking task')
    #create a coroutine for the blocking task 
    coro = asyncio.to_thread(blocking_task)
    #schedule the task 
    task = asyncio.create_task(coro)
    #retport a message 
    print(f'{time.ctime()} Main doing other things')
    #allow the schedul task to start 
    await asyncio.sleep(0)
    #awiat the task 
    await asyncio.sleep(0)
    #await the task
    await task 

#run the asyncio program
asyncio.run(main())


#result
Wed Jul 12 15:37:52 2023 Main running the blocking task
Wed Jul 12 15:37:52 2023 Main doing other things
Wed Jul 12 15:37:52 2023 Task starting...
Wed Jul 12 15:37:54 2023 Task done