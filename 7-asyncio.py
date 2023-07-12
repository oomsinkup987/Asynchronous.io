#example of using asyncio shiekd to protect a task from cancellation 
import time 
import asyncio

#define a simple asynchronous
async def simple_task(number):
    #block for a moment 
    await asyncio.sleep(1)
    #return the task 
    return number


#cancel the given task after a moment
async def cancel_task(task):
    #block for a moment
    await asyncio.sleep(0.2)
    #cancel the task 
    was_canceled = task.cancel()
    print(f'{time.ctime()} canceled: {was_canceled}')

#define a simple coroutine
async def main():
    #create coroutine 
    coro = simple_task(1)
    #create task 
    task = asyncio.create_task(coro)
    #create the shielded task 
    shieled = asyncio.shield(task)
    #create the task to cancel the previous task 
    asyncio.create_task(cancel_task(shieled))
    #handel cacellation
    try:
        #await the shielded task 
        result = await shieled
        print(f'{time.ctime()} >got: {result}')
    except asyncio.CancelledError:
        print(f'{time.ctime()} shielded was cancel')

    #wait a moment
    await asyncio.sleep(1)
    #report the detail of the task 
    print(f'{time.ctime()} shielded: {shieled}')
    print(f'{time.ctime()} task: {task}')

#start the loop 
asyncio.run(main())



#result 
Wed Jul 12 15:30:54 2023 canceled: True
Wed Jul 12 15:30:54 2023 shielded was cancel