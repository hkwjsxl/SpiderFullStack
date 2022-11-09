import requests

url = 'https://shici.store/huajianji/www/list/%E5%94%90%E8%AF%97%E4%B8%89%E7%99%BE%E9%A6%96.html'

proxy = {
    'https': 'http://127.0.0.1:7890',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
print(res.text)


