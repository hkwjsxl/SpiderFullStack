from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests


def get_sign(word):
    with open('get_sign.js', 'r', encoding='utf-8') as f:
        js = execjs.compile(f.read())
        return js.call('getSign', word)


def send_req(sign, word):
    req_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    data = {
        "from": "en",
        "to": "zh",
        "query": word,
        "transtype": "enter",
        "simple_means_flag": "3",
        "sign": sign,
        "token": "7057fff4f1d8a88b9a2bffee66ce1950",
        "domain": "common"
    }
    res = requests.post(req_url, headers=headers, data=data)
    print(res.json())


def main():
    word = 'shit'
    sign = get_sign(word)
    print(sign)
    send_req(sign, word)
    ...


if __name__ == '__main__':
    headers = {
        'Referer': 'https://fanyi.baidu.com/',
        'Cookie': 'BAIDUID=9709893BE955AC56AFFDCABAFD2EBE2C:FG=1; BAIDUID_BFESS=9709893BE955AC56AFFDCABAFD2EBE2C:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664693200; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664693200; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZDE5YTdkZDBhZTc3MGU5Nzg0OTBjNzI0NDZjNjcxOTZiOTYwZjJkZTk4Y2E5M2ViYWQ3ZjZmMzk5MGQzMzFmNzQ5ZTZiMzkwMGJiZTI1YjZmZTA0Zjg3M2Y3NWQ3ZDgxOThlNWY1MGU0MzNmM2RhY2JiMWI5NjdkYWMxODA5MWE5NDRlODY3MDA0YzQ1NzY0YzdhMmFjNjVhNjJmNWQyMA==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    main()
