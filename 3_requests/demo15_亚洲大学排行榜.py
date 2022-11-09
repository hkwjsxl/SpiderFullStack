import time

import requests
from lxml import etree
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor


def get_collection():
    client = MongoClient(host='127.0.0.1', port=27017)
    db = client['spider']
    return db['AsiaUniversityRank']


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
    tr_list = tree.xpath('//table[@class="sticky-enabled"]/tbody/tr')
    data_list = []
    for tr in tr_list:
        rank = tr.xpath('./td//text()')[0]
        world_rank = tr.xpath('./td//text()')[1]
        university_name = tr.xpath('./td//text()')[2]
        data_dict = {
            '亚洲排名': rank,
            '世界排名': world_rank,
            '学校名称': university_name,
        }
        data_list.append(data_dict)
        print(data_dict)
    collection_name.insert_many(data_list)  # many速度要比one快


def run(url):
    parse_data(get_res(url).text)


if __name__ == '__main__':
    start_time = time.time()
    collection_name = get_collection()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for page in range(10):
            main_url = f'https://www.webometrics.info/en/Asia?page={page}'
            pool.submit(run, main_url)
    print(time.time() - start_time)
