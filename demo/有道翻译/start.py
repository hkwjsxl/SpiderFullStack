import random

import requests
import time
from hashlib import md5

def enc_md5(e):
    md5_obj = md5()
    md5_obj.update(e.encode('utf-8'))
    return md5_obj.hexdigest()



def main():
    word = 'word'
    bv = enc_md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
    ts = str(int(time.time()*1000))
    salt = ts + str(random.randint(1, 9))
    sign = enc_md5("fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5")

    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        "i": "word",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "lts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=244456588@10.110.96.154; OUTFOX_SEARCH_USER_ID_NCOO=1870617237.6221073; JSESSIONID=abcqpK8UXjTg6cQp0ajny; ___rl__test__cookies=1663378594185',
        'Referer': 'https://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = requests.post(url, data=data, headers=headers)
    print(res.text)

if __name__ == '__main__':
    main()
