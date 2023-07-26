import asyncio
import time 

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f'{time.ctime()} hello {i} done')

async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

#run a program and print time
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
