import requests
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64
import json
from concurrent.futures.thread import ThreadPoolExecutor
from pymongo import MongoClient


def get_conn():
    client = MongoClient(host='localhost', port=27017)
    return client['spider']['zhaobiao']


def dec_des(enc_data):
    key = b"ctpstp@c"
    b64_data = base64.b64decode(enc_data)
    des = DES.new(key=key, mode=DES.MODE_ECB)
    src_data = des.decrypt(b64_data)
    return unpad(src_data, 8).decode('utf-8')


def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    src_data = dec_des(res.text)
    src_data = json.loads(src_data)
    print(src_data)
    conn.insert_one(src_data)


if __name__ == '__main__':
    conn = get_conn()
    with ThreadPoolExecutor(max_workers=32) as pool:
        for page in range(1, 6):
            url = f'https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/{page}'
            pool.submit(main, url)
