import requests

url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=1f277939918d27f4'
proxy = {
    'https': 'http://127.0.0.1:7890'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
data = {
    'from': 'zh',
    'to': 'en',
    'q': '知识'
}
res = requests.post(url=url, headers=headers, proxies=proxy, data=data)
print(res.json()['content']['out'])
