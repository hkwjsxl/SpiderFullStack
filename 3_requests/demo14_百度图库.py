import os.path
import re
import time

import requests
import asyncio
import aiohttp
import aiofiles


async def download(url_list):
    tasks = []
    for url in url_list:
        tasks.append(asyncio.create_task(download_one(url)))
    await asyncio.wait(tasks)


async def download_one(url):
    try:
        file_name = re.search('u=(?P<name>.*?)&fm', url).group('name')
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                content = await res.content.read()
                async with aiofiles.open(f'{file_path}/{file_name}.JPEG', 'wb') as f:
                    await f.write(content)
                print(f'{file_name}---下载完成!')
    except Exception as e:
        print(e)


def run():
    main_url = 'https://image.baidu.com/search/acjson'
    for page in range(5):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        proxy = {
            'https': 'http://127.0.0.1:7890'
        }
        data = {
            'tn': 'resultjson_com',
            'logid': '5786339055534724469',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'fr': '',
            'word': '索隆头像',
            'queryWord': '索隆头像',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf - 8',
            'oe': 'utf - 8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'expermode': '',
            'nojc': '',
            'isAsync': '',
            'pn': (page + 1) * 30,
            'rn': 30,
            'gsm': '96',
            '1657197758358': '',
        }
        res = requests.get(main_url, headers=headers, proxies=proxy, params=data)
        json_data = res.json()
        data_list = json_data['data']
        url_list = []
        for data in data_list[:-1]:  # 最后一个为None
            url_list.append(data.get('hoverURL'))
        asyncio.get_event_loop().run_until_complete(download(url_list))


if __name__ == '__main__':
    start_time = time.time()
    file_path = '百度图库'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    run()
    print(time.time() - start_time)
