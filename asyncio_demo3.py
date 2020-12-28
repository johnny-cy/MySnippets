async def foo():
    return 1

# print(foo()) #coroutine object foo at 0x7fece153ed40> 調用返回一個coroutine對象


import asyncio
import time
st = time.time()
all_apples = [1,1,1,1,1]
# 要求補貨
async def ask_for_apples(num):
    await asyncio.sleep(5)
    all_apples.append(num)

# 拿蘋果
async def take_apples(num):
    count = 0
    while count != num:
        if len(all_apples) == 0:
            await ask_for_apples(1)
        else:
            apple = all_apples.pop()
            count += 1
            yield apple

# 蘋果放入購物籃
async def buy_apples():
    bucket = []
    async for p in take_apples(10):
        bucket.append(p)
        print(bucket)
# buy_apples()

# 先把相關的方法都變成coroutine方法, async + await搭配使用
# coroutine方法中有使用for迴圈的，前面都要加async
# 原本若有使用time.sleep改成asyncio.sleep
# 執行時要用get_event_loop先建出一個loop 並用他的run_until_complete(fun)執行方法才能生效
loop = asyncio.get_event_loop()
res = loop.run_until_complete(buy_apples())
loop.close()
et = time.time()
print(et - st)