import os.path

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_res(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    res = requests.get(url, headers=headers, proxies=proxy)
    res.encoding = res.apparent_encoding
    return res


def parse_data(html_data):
    tree = etree.HTML(html_data)
    box_list = tree.xpath('//div[@class="layui-col-sm3 layui-col-xs6"]')
    for box in box_list:
        src = 'https:' + box.xpath('./a/img/@src')[0]
        _title = src.split('.')[-1]
        title = box.xpath('./a/img/@alt')[0]
        title = title + '.' + _title
        content = get_res(src).content
        save_data(title, content)


def save_data(title, content):
    with open(f'{file_path}/{title}.jpg', 'wb') as f:
        f.write(content)
    print(f'{title}---下载完成!')


def run(url):
    parse_data(get_res(url).text)


if __name__ == '__main__':
    file_path = '爱斗图'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with ThreadPoolExecutor(16) as pool:
        for page in range(1, 6):
            main_url = f'https://aidotu.com/search/0-0-0-{page}.html'
            pool.submit(run, main_url)
