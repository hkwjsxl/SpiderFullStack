import os.path

import requests
from lxml import etree
from urllib.parse import urljoin


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
    title = tree.xpath('//h1//text()')[0]
    # print(title)
    li_list = tree.xpath('//div[@class="book-mulu"]/ul/li')
    for li in li_list:
        sub_title = li.xpath('./a//text()')[0]
        href = li.xpath('./a/@href')[0]
        href = urljoin(url, href)
        # print(sub_title, href)
        sub_data = get_res(href).text
        tree = etree.HTML(sub_data)
        content = tree.xpath('//div[@class="card bookmark-list"]/div//text()')
        with open(f'{path}/{sub_title}.text', 'w', encoding='utf-8') as f:
            f.write(f'{sub_title}\n\n')
            for i in content:
                f.write(i.strip())
                f.write('\n')
        print(f'{sub_title}---下载完成!')


def run(url):
    html_data = get_res(url).text
    parse_data(html_data)


if __name__ == '__main__':
    path = '三国演义'
    if not os.path.exists(path):
        os.mkdir(path)
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    run(url)
