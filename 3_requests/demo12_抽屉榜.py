import requests
from lxml import etree


def get_res(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    proxy = {
        'https': 'http://127.0.0.1:7890'
    }
    res = requests.get(url, headers=headers, proxies=proxy)
    res.encoding = res.apparent_encoding
    return res


def parse_data(page_source):
    tree = etree.HTML(page_source)
    box = tree.xpath('//div[@class="link-con"]/div/div[@class="link-area clearfix"]/div[@class="link-info-con left"]')
    for item in box:
        detail = item.xpath('./div[@class="link-detail"]/a//text()')[0]
        href = item.xpath('./div[@class="link-detail"]/a/@href')[0]
        if not href.startswith('https'):
            href = 'https://dig.chouti.com' + href
        author = item.xpath('./div[@class="operate-author-con clearfix"]/div[@class="author-con left clearfix"]/span[1]/span//text()')[0]
        date_info = item.xpath('./div[@class="operate-author-con clearfix"]/div[@class="author-con left clearfix"]/span[2]/span//text()')[0] + '入榜'
        print(author, date_info, detail, href)


def run():
    main_url = 'https://dig.chouti.com/'
    res = get_res(main_url)
    parse_data(res.text)


if __name__ == '__main__':
    run()
