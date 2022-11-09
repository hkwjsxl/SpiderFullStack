from proxy_redis import ProxyRedis
from multiprocessing import Process
import asyncio
import aiohttp


async def check_one(red, proxy):
    timeout = aiohttp.ClientTimeout(total=5)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url='http://www.baidu.com', proxy='http://' + proxy, timeout=timeout) as res:
                await res.text()
                if res.status in [200, 302]:
                    print(proxy, '可用')
                    red.set_max_score(proxy)
                else:
                    print(proxy, '不可用')
                    red.desc_incrby(proxy)
    except Exception as e:
        print(e)
        red.desc_incrby(proxy)


async def check(red):
    all_proxy = red.get_all_proxy()
    tasks = []
    for proxy in all_proxy:
        tasks.append(asyncio.create_task(check_one(red, proxy)))
    if tasks:
        await asyncio.wait(tasks)


def run():
    red = ProxyRedis()
    asyncio.run(check(red))


if __name__ == '__main__':
    Process(target=run, ).start()


