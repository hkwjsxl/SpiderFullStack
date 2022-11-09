from proxy_redis import ProxyRedis
import requests
from lxml import etree
from multiprocessing import Process
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def jiangxianli(red):
    url = 'https://ip.jiangxianli.com/?page=1'
    res = requests.get(url=url, headers=headers).text
    tree = etree.HTML(res)
    tr_list = tree.xpath('//table//tr')
    for tr in tr_list:
        ip = tr.xpath('./td[1]/text()')
        port = tr.xpath('./td[2]/text()')
        if not ip:
            continue
        ip = ip[0]
        port = port[0]
        proxy = ip + ':' + port
        print(proxy)
        red.add_proxy_id(proxy)


def run():
    while True:
        try:
            red = ProxyRedis()
            jiangxianli(red)
        except Exception as e:
            print(e)
        time.sleep(60)


if __name__ == '__main__':
    Process(target=run).start()






