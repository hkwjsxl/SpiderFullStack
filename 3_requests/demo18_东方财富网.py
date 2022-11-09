import requests
import time
from concurrent.futures import ThreadPoolExecutor
from pymongo import MongoClient


def get_collection():
    client = MongoClient(host='127.0.0.1', port=27017)
    collection = client['spider']['DongFangcaipiao']
    return collection


def get_res(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    data = {
        'pz': '20',
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'wbp2u': '| 0 | 0 | 0 | web',
        'fid': 'f3',
        'fs': 'm:0 t:6,m:0 t:80,m:1 t:2,m:1 t:23,m:0 t:81 s:2048',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152',
        '_': int(time.time() * 1000)
    }
    res = requests.get(url, headers=headers, proxies=proxy, params=data)
    res.encoding = res.apparent_encoding
    return res


def parse_data(page_source, collection):
    data_list = page_source['data']['diff']
    lst = []
    for data in data_list:
        name = data['f14']
        new_price = data['f2']
        sale_num = data['f5']
        sale_price = data['f6']
        amplitude = data['f7']
        data_dict = {
            '名称': name,
            '最新价': new_price,
            '成交量': sale_num,
            '成交额': sale_price,
            '振幅': amplitude,
        }
        lst.append(data_dict)
    print(lst)
    collection.insert_many(lst)


def run(url, collection):
    parse_data(get_res(url).json(), collection)


if __name__ == '__main__':
    collection = get_collection()
    with ThreadPoolExecutor(32) as pool:
        for page in range(1, 11):
            main_url = f'http://7.push2.eastmoney.com/api/qt/clist/get?pn={page}'
            pool.submit(run, main_url, collection)
