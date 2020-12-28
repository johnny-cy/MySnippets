import asyncio
import time

now = lambda: time.time()

async def dosomething(num):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))

if __name__ == "__main__":
    start = time.time()
    print(asyncio.iscoroutinefunction(dosomething))
    tasks = [dosomething(i) for i in range(500)] # 執行coroutine 函數
    asyncio.run(asyncio.wait(tasks))
    print('TIME: ', time.time() - start)

"""
由結果可知，500個作業都同時執行完了第一步，之後500個在同時執行第二步，可知道500個是接近同時地併發!
"""