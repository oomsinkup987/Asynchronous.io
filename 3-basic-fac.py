import asyncio
import time 

async def factorial(n):
    f = 1 
    for i in range(2, n + 1):
        print(f'Computime factorial({n}, curently i={i}...)')
        await asyncio.sleep(1)
        f *= i
    return f
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L) #[2,6,24]

if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')