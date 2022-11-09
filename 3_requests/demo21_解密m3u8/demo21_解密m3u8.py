import os.path
import re

import requests
import aiohttp
import aiofiles
import asyncio
from urllib.parse import urljoin


def get_m3u8_data(main_url, url):
    session = requests.Session()
    session.get(main_url, headers=headers)
    first_page_source = session.get(url, headers=headers).text
    index_m3u8_url = first_page_source.split('\n')[-2].strip()
    index_m3u8_url = urljoin(main_url, index_m3u8_url)
    second_page_source = session.get(index_m3u8_url, headers=headers).text
    with open('index.m3u8', mode='w', encoding='utf-8') as f:
        for line in second_page_source:
            f.write(line)


async def down_all_ts():
    with open('index.m3u8', 'r', encoding='utf-8') as f:
        data = f.readlines()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for line in data:
            if line.startswith('#'):
                continue
            ts_name = line.split('/')[-1].strip()
            ts_url = urljoin(main_url, line.strip())
            task = asyncio.create_task(down_one_ts(session, ts_url, ts_name))
            tasks.append(task)
        await asyncio.gather(*tasks)


async def down_one_ts(session, ts_url, ts_name):
    for i in range(10):
        try:
            async with session.get(ts_url) as res:
                content = await res.content.read()
                async with aiofiles.open(f'{path}/{ts_name}', mode='wb') as f:
                    await f.write(content)
                print(ts_name, '下载完成!')
                break
        except Exception as e:
            print(e)
            print(ts_name, '下载失败!')


def do_ts():
    with open('index.m3u8', 'r', encoding='utf-8') as f:
        data = f.readlines()
    current_path = os.getcwd()
    os.chdir('./ts/')
    with open('index.m3u8', 'w', encoding='utf-8') as ts_file, open('key.m3u8', 'w', encoding='utf-8') as key_file:
        for line in data:
            if line.startswith('#'):
                if line.find('URI') != -1:
                    key_url = re.search('URI="(.*?)"', line).group(1)
                    key_url = urljoin(main_url, key_url)
                    key_data = requests.get(key_url, headers=headers).text
                    key_file.write(key_data)
                    line = line.split('/')[0] + 'key.m3u8"\n'
                ts_file.write(line)
            else:
                ts_local_path = os.path.join(os.getcwd(), line.split('/')[-1])
                ts_file.write(ts_local_path)
    os.chdir(current_path)


def merge(filename='output'):
    os.chdir('./ts/')
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)


if __name__ == '__main__':
    path = 'ts'
    if not os.path.exists(path):
        os.mkdir(path)
    main_url = 'https://s7.fsvod1.com'
    url = 'https://s7.fsvod1.com/20220622/5LnZiDXn/index.m3u8'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    get_m3u8_data(main_url, url)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(down_all_ts())

    do_ts()
    merge()


