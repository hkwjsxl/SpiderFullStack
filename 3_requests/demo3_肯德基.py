import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
for page in range(1, 11):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': page,
        'pageSize': '10',
    }
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'Cookie': 'll="118091"; bid=XFRsLwrz81M; push_noty_num=0; push_doumail_num=0; dbcl2="249449316:gjeVE/jJwlY"; ct=y; ck=_VCi; ap_v=0,6.0',
        'Referer': 'https://movie.douban.com/explore',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    res = requests.post(url=url, headers=headers, proxies=proxy, data=data)
    tables = res.json()['Table1']
    for row in tables:
        name = row['storeName']
        address = row['addressDetail']
        info = row['pro']
        print(name, address, info)
    print(f'{page}---over'.center(50, '-'))

