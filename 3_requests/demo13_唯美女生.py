import os
import time

import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process


class WeiMmeiNS:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        self.proxy = {
            'https': 'http://127.0.0.1:7890'
        }
        self.file_path = '唯美女生'
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)

    def get_res(self, url):
        res = requests.get(url, headers=self.headers, proxies=self.proxy)
        res.encoding = res.apparent_encoding
        return res

    def parse_data(self, page_source):
        tree = etree.HTML(page_source)
        href_list = tree.xpath('//div[@class="list-content"]/div/a/@href')
        title_list = tree.xpath('//div[@class="list-content"]/div/a/@title')
        return href_list, title_list

    async def download(self, url_list, title_list):
        for url, title in zip(url_list, title_list):
            sub_page_source = self.get_res(url).text
            tree = etree.HTML(sub_page_source)
            img_url_list = tree.xpath('//div[@class="nc-light-gallery"]/a[@rel="nofollow"]/@href')
            tasks = []
            for img_url in img_url_list:
                tasks.append(asyncio.create_task(self.download_one(title, img_url)))
            await asyncio.wait(tasks)

    async def download_one(self, title, img_url):
        if not os.path.exists(f'{self.file_path}/{title}'):
            os.mkdir(f'{self.file_path}/{title}')
        async with aiohttp.ClientSession() as session:
            async with session.get(url=img_url) as resq:
                content = await resq.content.read()
                name = img_url.split('/')[-1]
                async with aiofiles.open(f'{self.file_path}/{title}/{name}', 'wb') as f:
                    await f.write(content)
                print(f'{name}---下载完成!')

    def run(self, url):
        res = self.get_res(url)
        href_list, title_list = self.parse_data(res.text)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.download(href_list, title_list))


if __name__ == '__main__':
    start_time = time.time()
    weimeins = WeiMmeiNS()
    for page in range(1, 3):
        main_url = f'https://www.vmgirls.com/pure/page/{page}/'
        weimeins.run(main_url)

