#example of waiting for all task to complete 
import random
import asyncio
import time 

#coroutine to execute in a new task 
async def task_coro(arg):
    #generate a random value between 0 and 1 
    value = random.random()
    #block for a moment 
    await asyncio.sleep(value)
    #retport the value 
    print(f' {time.ctime()} > task {arg} done with {value}')

#main coroutine 
async def main():
    #create many task 
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    #wait for all task to complete # ALL_COMPLETE, FIRST_COMPLETE, FIRST_EXCEPTED
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    #report 
    print(f'{time.ctime()} ALL done')

#start the asyncio program
asyncio.run(main())


#Result ALL_COMPLETED
Wed Jul 12 15:04:20 2023 > task 8 done with 0.131661425192099
 Wed Jul 12 15:04:20 2023 > task 3 done with 0.1899912325687284
 Wed Jul 12 15:04:20 2023 > task 5 done with 0.2619832275794848
 Wed Jul 12 15:04:20 2023 > task 1 done with 0.30947835025016257
 Wed Jul 12 15:04:20 2023 > task 2 done with 0.32563474311980667
 Wed Jul 12 15:04:21 2023 > task 6 done with 0.3993663453020363
 Wed Jul 12 15:04:21 2023 > task 9 done with 0.7076033300308036
 Wed Jul 12 15:04:21 2023 > task 0 done with 0.9653272375875449
 Wed Jul 12 15:04:21 2023 > task 7 done with 0.969971319482578
 Wed Jul 12 15:04:21 2023 > task 4 done with 0.9742412707488082
Wed Jul 12 15:04:21 2023 ALL done


#FIRST_COMPLETED
Wed Jul 12 15:05:36 2023 > task 9 done with 0.023007395417112386
Wed Jul 12 15:05:36 2023 ALL done

#FIRST_EXCEPTED
 Wed Jul 12 15:06:33 2023 > task 5 done with 0.04841852944499525
 Wed Jul 12 15:06:33 2023 > task 3 done with 0.09171487901163966
Wed Jul 12 15:06:33 2023 ALL done