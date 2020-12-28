import asyncio
import random


"""
本次使用到的方法如下：
asyncio.ensure_future()
asyncio.asyncio.sleep()
asyncio.get_event_loop()
asyncio.get_event_loop().run_until_completed()
asyncio.get_event_loop().close()
asyncio.gather()

"""
async def myCoroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print("Coroutine {}, has successfully completed after {} seconds".format(id, process_time))

async def main():
    tasks = []
    for i in range(100):
        tasks.append(asyncio.ensure_future(myCoroutine(i))) # 直接先連續撒網100次
    await asyncio.gather(*tasks) # 然後去收網，等到全部收完再走下一步

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

"""
RESULT:
Coroutine 3, has successfully completed after 1 seconds
Coroutine 0, has successfully completed after 2 seconds
Coroutine 1, has successfully completed after 2 seconds
Coroutine 7, has successfully completed after 2 seconds
Coroutine 8, has successfully completed after 2 seconds
Coroutine 4, has successfully completed after 3 seconds
Coroutine 6, has successfully completed after 3 seconds
Coroutine 2, has successfully completed after 4 seconds
Coroutine 5, has successfully completed after 4 seconds
Coroutine 9, has successfully completed after 4 seconds
五秒內跑完10個至少等待1秒的作業，用這方式，即便是100個作業，也是5秒跑完
"""