import re

import requests
from lxml import etree

url = 'https://movie.douban.com/review/best/'
proxy = {
    'https': 'http://127.0.0.1:7890'
}
headers = {
    'Cookie': 'll="118091"; bid=XFRsLwrz81M; push_noty_num=0; push_doumail_num=0; dbcl2="249449316:gjeVE/jJwlY"; ct=y; ck=_VCi; ap_v=0,6.0',
    'Referer': 'http://localhost:63342/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
res = requests.get(url=url, proxies=proxy, headers=headers)
res.encoding = 'utf-8'
tree = etree.HTML(res.text)
data_list = tree.xpath('//div[@class="review-list chart "]/div')
for data in data_list:
    cid = data.xpath('./@data-cid')[0]
    href = data.xpath('./div/a/@href')[0]
    img_src = data.xpath('./div/a/img/@src')[0]
    title = data.xpath('./div/div/h2/a//text()')[0]
    info_list = data.xpath('./div/div/div/div//text()')
    if len(info_list) > 3:
        info = data.xpath('./div/div/div/div//text()')[2].replace(' ', '').replace('\n', '')
    else:
        info = data.xpath('./div/div/div/div//text()')[0].replace(' ', '').replace('\n', '')
    # print(cid, href, img_src, title, info)
    detail_url = f'https://movie.douban.com/j/review/{cid}/full'
    res = requests.get(url=detail_url, headers=headers, proxies=proxy)
    detail = res.json()['html']
    p_list = re.findall('<p data-align="">(.*?)</p>', detail)
    for p in p_list:
        print(p)
    break


