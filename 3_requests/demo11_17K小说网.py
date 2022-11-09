import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
proxy = {
    'https': 'http://127.0.0.1:7890'
}
data = {
    'loginName': '18533538210',
    'password': '20020224.'
}
login_url = 'https://passport.17k.com/ck/user/login'
session = requests.session()
session.post(url=login_url, headers=headers, proxies=proxy, data=data)
url = 'https://user.17k.com/www/bookshelf/'
res = session.get(url=url, headers=headers, proxies=proxy)
res.encoding = res.apparent_encoding
print(res.text)


