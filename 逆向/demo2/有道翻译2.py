from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

word = 'respect'

import execjs
f = open('ydfy.js', 'r', encoding='utf-8')
js = execjs.compile(f.read())
val = js.call('fn', word)
# print(val)


ts = val['ts']
bv = val['bv']
salt = val['salt']
sign = val['sign']

# print(ts)
# print(bv)
# print(salt)
# print(sign)

import requests

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1133959678@10.110.96.158; OUTFOX_SEARCH_USER_ID_NCOO=682140484.4863664; P_INFO=18533538210|1653201951|1|youdaonote|00&99|null&null&null#heb&130400#10#0|&0||18533538210; ___rl__test__cookies=1661152915526',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
res = requests.post(url, data=data, headers=headers)
print(res.json())


