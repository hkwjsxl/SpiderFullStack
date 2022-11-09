import requests
import aiohttp
import aiofiles
import asyncio
from lxml import etree
from urllib.parse import urljoin
import os


def get_all_detail_url(url):
    res = requests.get(url, headers=headers, proxies=proxy)
    res.encoding = res.apparent_encoding
    tree = etree.HTML(res.text)
    li_list = tree.xpath('//ul[@id="newlist"]/li')
    href_list = []
    for li in li_list:
        href = li.xpath('./a/@href')[0]
        href = urljoin(url, href)
        href_list.append(href)
    return href_list


async def down(url_list):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            tasks.append(asyncio.create_task(down_one(session, url)))
        await asyncio.wait(tasks)


async def down_one(session, url):
    async with session.get(url=url, headers=headers) as resp:
        html_data = await resp.text()
        tree = etree.HTML(html_data)
        title = tree.xpath('//div[@class="panel-heading"]//text()')[0]
        p_list = tree.xpath('//div[@id="content-txt"]/p')
        async with aiofiles.open(f'{path}/{title}.text', 'w', encoding='utf-8') as f:
            await f.write(f'{title}\n\n')
            for p in p_list:
                content = p.xpath('.//text()')[0]
                await f.write(f'{content}\n')
        print(f'{title}---下载完成!')


def run():
    main_url = 'https://www.biquc.com/26/26687/'
    href_list = get_all_detail_url(main_url)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(down(href_list))


if __name__ == '__main__':
    path = '请仙儿'
    if not os.path.exists(path):
        os.mkdir(path)
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    run()
