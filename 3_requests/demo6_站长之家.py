import os.path
import time

import requests
from lxml import etree
from urllib.parse import urljoin
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor


def get_res(url):
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, proxies=proxy)
    res.encoding = 'utf-8'
    return res


def parse_data(html_data):
    tree = etree.HTML(html_data)
    div_list = tree.xpath('//div[@id="container"]/div')
    for div in div_list:
        href = urljoin(url, div.xpath('./p/a/@href')[0])
        sub_html = get_res(href).text
        tree = etree.HTML(sub_html)
        title = tree.xpath('//div[@class="imga"]/a/@title')[0]
        src = tree.xpath('//div[@class="imga"]/a/img/@src')[0]
        src = urljoin(url, src)
        content = requests.get(url=src, proxies={'https': 'http://127.0.0.1:7890'}).content
        # urlretrieve(src, f'{path}/{title}.jpg')  # 速度慢
        with open(f'{path}/{title}.jpg', 'wb') as f:
            f.write(content)
        print(f'{title}---下载完成!')


def run(url):
    html_data = get_res(url).text
    parse_data(html_data)


if __name__ == '__main__':
    start_time = time.time()
    path = '站长之家'
    if not os.path.exists(path):
        os.mkdir(path)
    with ThreadPoolExecutor(max_workers=16) as pool:
        for i in range(1, 6):
            if i == 1:
                url = 'https://sc.chinaz.com/tupian/fengjingtupian.html'
            else:
                url = f'https://sc.chinaz.com/tupian/fengjingtupian_{i}.html'
            pool.submit(run, url)
            print(f'{i}页爬取成功'.center(50, '-'))
            break
    # print(time.time() - start_time)
    # 34.02882957458496
    # 96.13784599304199

