import requests
from lxml import etree
import os


def get_res(url):
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, proxies=proxy)
    res.encoding = res.apparent_encoding
    return res


def parse_data(html_data):
    tree = etree.HTML(html_data)
    mulu_list = tree.xpath('//div[@class="mulu"]')
    for mulu in mulu_list:
        tr_list = mulu.xpath('./center/table/tr')
        title = tr_list[0].xpath('./td/center/h2/a//text()')[0]
        if not os.path.exists(title):
            os.mkdir(title)
        for tr in tr_list[1:]:
            chapters = tr.xpath('./td/a//text()')
            hrefs = tr.xpath('./td/a/@href')
            for chapter, href in zip(chapters, hrefs):
                parse_sub_data(title, chapter, href)
        break


def parse_sub_data(title, chapter, href):
    html_data = get_res(href).text
    tree = etree.HTML(html_data)
    p_list = tree.xpath('//div[@class="content"]/p')[:-1]
    for p in p_list:
        content = p.xpath('.//text()')[0]
        save_data(title, chapter, content)
    print(f'{title}---{chapter}下载完成!')


def save_data(title, chapter, content):
    with open(f'{title}/{chapter}.text', 'a', encoding='utf-8') as f:
        f.write(f'{content}\n')


def run(url):
    parse_data(get_res(url).text)


if __name__ == '__main__':
    main_url = 'https://www.mingchaonaxieshier.com/'
    run(main_url)
