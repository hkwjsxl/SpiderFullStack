import requests
import time
import base64
import json
import hmac
from hashlib import md5, sha256


def enc_md5(e):
    e = e.encode('utf-8')
    md5_obj = md5()
    md5_obj.update(e)
    return md5_obj.digest()


def enc_b64(e):
    return base64.b64encode(e).decode()


def enc_sha256(e):
    e = e.encode('utf-8')
    sha256_obj = sha256()
    sha256_obj.update(e)
    return sha256_obj.digest()

def enc_hmac(e, key):
    return hmac.new(key=key.encode('utf-8'), msg=e.encode('utf-8'), digestmod=sha256).digest()

def main():
    data = {
        "keyword": "高校",
        "pageNum": 1,
        "type": -1,
        "pageSize": 15
    }
    json_data = json.dumps(data)
    # md5_result = enc_md5(json_data)
    # b64_result = enc_b64(md5_result)
    b64_result = 'WQReRVBLFGvLpuu+MZJYVQ=='
    print(b64_result)
    now_time = str(int(time.time() * 1000))
    v = f'POST\nhttps://gdtv-api.gdtv.cn/api/search/v1/news\n{now_time}\n{b64_result}'
    signature = enc_hmac(v, 'dfkcY1c3sfuw0Cii9DWjOUO3iQy2hqlDxyvDXd1oVMxwYAJSgeB6phO8eW1dfuwX')
    print(signature)
    signature = enc_b64(signature)
    print(signature)
    # sha256_result = enc_sha256(v)
    # signature = enc_b64(sha256_result)

    url = 'https://gdtv-api.gdtv.cn/api/search/v1/news'
    headers = {
        'referer': 'https://www.gdtv.cn/',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        "x-itouchtv-ca-key": "89541443007807288657755311869534",
        "x-itouchtv-ca-signature": signature,
        "x-itouchtv-ca-timestamp": now_time,
        "x-itouchtv-client": "WEB_PC",
        "x-itouchtv-device-id": "WEB_0f6bd800-3a1a-11ed-9746-193e7b21bd8b"
    }
    res = requests.post(url, headers=headers, data=json_data)
    print(res.text)


if __name__ == '__main__':
    main()



