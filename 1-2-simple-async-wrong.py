# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.01
# Task B: Computing 1+2
# Time: 3.01
# Task B: Computing 3+3
# Time: 4.02
# Task B: Sum = 6

# Time: 5.03 sec
import asyncio
import time
#ฟังก์ชั่น sleep() ให้รอ 1 วินาที 
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        # คำนวณผลรวมตัวเลข
        total += number
         # แสดงข้อความการคำนวณและตัวเลขที่ใช้ในการคำนวณ
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
   #กำหนดค่าที่จะแสดงผลลัพท์และเรียกใช้ค่าsum
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
#รันloop asyncio.wait
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')
