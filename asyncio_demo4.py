import asyncio

import time
import random

# loop
# ready for all and then start together at once
# wait until completed

async def job(id):
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print(f"Thread id-{id} finished in {process_time} sec.")

async def main():
    tasks = []
    for i in range(1,50):
        tasks.append(asyncio.ensure_future(job(i))) # cowork with asyncio.gather
    await asyncio.gather(*tasks) #  等待tasks的資料不在變動

# main()

loop = asyncio.get_event_loop()
loop.run_until_complete(main()) 
loop.close()