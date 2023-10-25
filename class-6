import asyncio
import time

class Coffee:
    pass

class Egg:
    pass

class Toast:
    pass

async def PourCoffee():
    print(f"{time.ctime()} - Pouring coffee")
    
    print("Coffee is ready")
    return Coffee()

async def ApplyButter():
    print(f"{time.ctime()} - Spreading butter on toast")
    await asyncio.sleep(1)

async def FryEggsAsync(howMany):
    print(f"{time.ctime()} - Heat pan to fry eggs")
    await asyncio.sleep(3)
    print("Frying", howMany, "eggs")
    await asyncio.sleep(3)
    print("Eggs are ready")
    return Egg()

async def ToastAsync(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        await asyncio.sleep(3)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        await ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    return Toast()

async def main():
    coffee = await PourCoffee()
    await asyncio.gather(FryEggsAsync(2), ToastAsync(2))
    print(f"{time.ctime()} - Breakfast is ready!")

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{time.ctime()} - Breakfast cooked in", elapsed, "seconds.")
