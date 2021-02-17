import asyncio
from asyncio.tasks import ensure_future
import time
import random

async def job(id):
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print(f"Coroutine {id} has done after {process_time} sec.")
    return id*10
async def main():
    tasks = []
    for id in range(1,10):
        tasks.append(asyncio.ensure_future(job(id)))
    await asyncio.gather(*tasks)
    tasks = [ task.result() for task in tasks ]
    print(tasks)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

loop.close()


# 1. 起手式
"""
loop = asyncio.get_event_loop()
loop.run_until.complete(main())
loop.close()
"""
# 2. 定義執行job的方法, 讓job同時被執行, 然後統一等他們跑完
"""
async def main():
    tasks = []
    for i in range(1,10):
        tasks.append(asyncio.ensure_future(job(i)))
    asyncio.gather(*tasks)
"""
# 3. 定義job 
"""
async def job(id):
    pass
"""