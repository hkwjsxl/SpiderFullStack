from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

from hashlib import md5
import time
import random

word = 'respect'

# import execjs
# f = open('ydfy.js', 'r', encoding='utf-8')
# js = execjs.compile(f.read())
# val = js.call('md5', word)
# print(val)


# var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
#         }
#     };

# data: {
#     i: e.i,
#     client: "fanyideskweb",
#     salt: i.salt,
#     sign: i.sign,
#     lts: i.ts,
#     bv: i.bv,
#     tgt: e.tgt,
#     modifiedTgt: e.modifiedTgt,
#     from: e.from,
#     to: e.to
# },

val = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
md5_obj = md5()
md5_obj.update(val.encode('utf-8'))
md5_val = md5_obj.hexdigest()

t = md5_val
r = str(int(time.time() * 1000))
i = r + str(random.randint(1, 10))

md5_obj1 = md5()
md5_obj1.update("fanyideskweb".encode('utf-8'))
md5_obj1.update(word.encode('utf-8'))
md5_obj1.update(i.encode('utf-8'))
md5_obj1.update("Ygy_4c=r#e#4EX^NUGUc5".encode('utf-8'))
md5_val1 = md5_obj1.hexdigest()

ts = r
bv = t
salt = i
sign = md5_val1

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


