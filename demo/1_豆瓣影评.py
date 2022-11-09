import os
import requests
from lxml import etree
from concurrent.futures.thread import ThreadPoolExecutor


def main(url):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    name_list = tree.xpath('//header[@class="main-hd"]/a[@class="name"]/text()')
    href_list = tree.xpath('//div[@class="main-bd"]/h2/a/@href')
    for name, href in zip(name_list, href_list):
        parse_sub(name, href)


def parse_sub(name, href):
    res = requests.get(href, headers=headers)
    tree = etree.HTML(res.text)
    article = tree.xpath('//div[@class="article"]')[0]
    movie_name = article.xpath('.//header[@class="main-hd"]/a/text()')[2]
    title = article.xpath('./h1/span/text()')[0]
    content = article.xpath('.//div[@id="link-report"]/div/p//text()')[0]
    save(name, movie_name, title, content)


def save(name, movie_name, title, content):
    with open(f'{file_path}/{movie_name}.txt', 'w', encoding='utf-8') as f:
        f.write(name + '\n')
        f.write(movie_name + '\n')
        f.write(title + '\n\n')
        f.write(content + '\n')
    print(movie_name, 'success')


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    file_path = '豆瓣影评'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    with ThreadPoolExecutor(max_workers=32) as pool:
        for page in range(0, 101, 20):
            main_url = f'https://movie.douban.com/review/best/?start={page}'
            pool.submit(main, main_url)
