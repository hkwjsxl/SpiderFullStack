from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs


def main():
    url = 'http://59.110.45.28/m/api/search'
    with open('myfreemmp3.js', 'r', encoding='utf-8') as f:
        js = execjs.compile(f.read())
    d = js.call('fn', '林俊杰')
    d = d.strip('data=')
    d = d.strip('&v=2')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    data = {
        'data': d,
        'v': '2'
    }
    res = requests.post(url, data=data, headers=headers)
    print(res.json())


if __name__ == '__main__':
    main()
