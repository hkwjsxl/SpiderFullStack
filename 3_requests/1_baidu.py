import requests

url = 'https://www.baidu.com'
proxy = {
    'https': 'http://127.0.0.1:7890'
}
res = requests.get(url=url, proxies=proxy)
# res.encoding = 'utf-8'
# print(res.text)

# print(res.content.decode('utf-8'))

# print(res.ok)
# print(res.status_code)
# print(res.url)
# print(res.headers)
# print(res.cookies.items())
