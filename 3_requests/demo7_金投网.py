import requests
from lxml import etree


def get_res(url):
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers, proxies=proxy)
    res.encoding = 'utf-8'
    return res


def run(url):
    html_data = get_res(url).text
    tree = etree.HTML(html_data)
    table = tree.xpath('//table')[1]
    tr_list = table.xpath('./tbody/tr')
    for tr in tr_list:
        for td in tr.xpath('./td//text()'):
            print(td)


if __name__ == '__main__':
    url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'
    run(url)
