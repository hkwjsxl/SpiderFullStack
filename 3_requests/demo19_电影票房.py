import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text


def parse_html(html):
    try:
        tree = etree.HTML(html)
        trs = tree.xpath("//table/tbody/tr")[1:]
        result = []
        for tr in trs:
            year = tr.xpath("./td[2]//text()")
            year = year[0] if year else ""
            name = tr.xpath("./td[3]//text()")
            name = name[0] if name else ""
            money = tr.xpath("./td[4]//text()")
            money = money[0] if money else ""
            d = (year, name, money)
            if any(d):
                result.append(d)
        return result
    except Exception as e:
        print(e)


def download_one(url, f):
    page_source = get_page_source(url)
    data = parse_html(page_source)
    for item in data:
        f.write(",".join(item))
        f.write("\n")


def main():
    f = open("movie.csv", mode="w", encoding='utf-8')
    lst = [str(i) for i in range(1994, 2022)]
    with ThreadPoolExecutor(10) as t:
        # 方案一
        # for year in lst:
        #     url = f"http://www.boxofficecn.com/boxoffice{year}"
        #     # download_one(url, f)
        #     t.submit(download_one, url, f)

        # 方案二
        t.map(download_one, (f"http://www.boxofficecn.com/boxoffice{year}" for year in lst),
              (f for i in range(len(lst))))


if __name__ == '__main__':
    main()
