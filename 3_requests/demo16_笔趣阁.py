import requests
from lxml import etree
import os
import asyncio
import aiofiles
import aiohttp
from urllib.parse import urljoin


class DouLuoDaLu():
    def __init__(self):
        self.proxy = {
            'https': 'http://127.0.0.1:7890'
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        self.path = '斗罗大陆5'
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.main_url = 'https://www.xbiquwx.la/80_80807/'

    def get_res(self, url):
        res = requests.get(url, headers=self.headers, proxies=self.proxy)
        res.encoding = res.apparent_encoding
        return res

    def parse_main_page(self, page_source):
        tree = etree.HTML(page_source)
        dd_list = tree.xpath('//div[@id="list"]/dl/dd')
        title_list = []
        href_list = []
        for dd in dd_list:
            title = dd.xpath('./a/@title')[0]
            href = dd.xpath('./a/@href')[0]
            href = urljoin(self.main_url, href)
            title_list.append(title)
            href_list.append(href)
        return title_list, href_list

    async def download(self, title_list, href_list):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for title, url in zip(title_list, href_list):
                tasks.append(asyncio.create_task(self.download_one(session, title, url)))
            await asyncio.wait(tasks)

    async def download_one(self, session, title, url):
        async with session.get(url, headers=self.headers) as res:
            page_source = await res.text()
            tree = etree.HTML(page_source)
            content = tree.xpath('//div[@id="content"]//text()')
            async with aiofiles.open(f'{self.path}/{title}.text', 'w', encoding='utf-8') as f:
                await f.write(f'{title}\n')
                for i in content:
                    await f.write(i.replace(' ', '') + '\n')
            print(title, '下载完成')

    def run(self):
        page_source = self.get_res(self.main_url).text
        title_list, href_list = self.parse_main_page(page_source)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.download(title_list, href_list))


if __name__ == '__main__':
    douluodalu = DouLuoDaLu()
    douluodalu.run()
