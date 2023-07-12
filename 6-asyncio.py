#example of waiting for all task to complete 
from random import random
import asyncio
import time 

#coroutine to execute in a new task 
async def task_coro(arg):
    #generate a random value between 0 and 1 
    value = 1 + random()
    #report message
    print(f' {time.ctime()} > task got {value}')
    #block for a moment 
    await asyncio.sleep(value)
    #retport all time 
    print(f' {time.ctime()} > task done')

#main coroutine 
async def main():
    #create many task 
    tasks = task_coro(1)
    #ececute and wait for the task without a timeout
    try:
        await asyncio.wait_for(tasks,timeout=0.2)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gavve up waiting, task canceled')

#start the asyncio program
asyncio.run(main())


#Result

Wed Jul 12 15:12:19 2023 > task got 1.9519734312945476
Wed Jul 12 15:12:19 2023 Gavve up waiting, task canceled
