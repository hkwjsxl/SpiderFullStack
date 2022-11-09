import requests

# url = 'https://movie.douban.com/explore'
url = 'https://movie.douban.com/j/search_subjects'
for i in range(5):
    data = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': i * 20,
    }
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'Cookie': 'll="118091"; bid=XFRsLwrz81M; push_noty_num=0; push_doumail_num=0; dbcl2="249449316:gjeVE/jJwlY"; ct=y; ck=_VCi; ap_v=0,6.0',
        'Referer': 'https://movie.douban.com/explore',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    res = requests.get(url=url, proxies=proxy, headers=headers, params=data)
    subjects = res.json()['subjects']
    for sub in subjects:
        title = sub['title']
        detail = sub['url']
        print(title, detail)
    print(f'{i+1}-over'.center(50, '-'))