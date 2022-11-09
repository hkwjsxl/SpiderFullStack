import requests
from lxml import etree
from pandas.io.excel import ExcelWriter
import pandas as pd
import csv


def main():
    url = 'https://zh.moegirl.org.cn/2014%E5%B9%B4%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86%E5%8A%A8%E7%94%BB%E7%94%B5%E5%BD%B1%E7%A5%A8%E6%88%BF'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    with open('电影票房.csv', 'w', encoding='utf-8') as f:
        row_head = tree.xpath('//table[@class="wikitable sortable"]/tbody/tr/th/text()')
        csv_writer = csv.DictWriter(f, fieldnames=[
            row_head[0], row_head[1], row_head[2], row_head[3], row_head[4], row_head[5], row_head[6],
            row_head[7].strip()
        ])
        csv_writer.writeheader()

        trs = tree.xpath('//table[@class="wikitable sortable"]/tbody/tr')[1:]
        for tr in trs:
            if len(tr.xpath('./td[6]//text()')) == 4:
                create_date = tr.xpath('./td[6]//text()')[1] + tr.xpath('./td[6]//text()')[3]
            elif len(tr.xpath('./td[6]//text()')) == 3:
                create_date = tr.xpath('./td[6]//text()')[0] + tr.xpath('./td[6]//text()')[2]
            elif len(tr.xpath('./td[6]//text()')) == 2:
                create_date = tr.xpath('./td[6]//text()')[1]
            else:
                create_date = tr.xpath('./td[6]//text()')[0]
            data_dic = {
                row_head[0]: tr.xpath('./td[1]/text()')[0],
                row_head[1]: tr.xpath('./td[2]//text()')[0],
                row_head[2]: tr.xpath('./td[3]//text()')[1] if len(tr.xpath('./td[3]//text()')) == 2 else
                tr.xpath('./td[3]//text()')[0],
                row_head[3]: tr.xpath('./td[4]//text()')[1] if len(tr.xpath('./td[4]//text()')) == 2 else
                tr.xpath('./td[4]//text()')[0],
                row_head[4]: tr.xpath('./td[5]//text()')[1] if len(tr.xpath('./td[5]//text()')) == 2 else
                tr.xpath('./td[5]//text()')[0],
                row_head[5]: create_date,
                row_head[6]: tr.xpath('./td[7]//text()')[0],
                row_head[7].strip(): tr.xpath('./td[8]//text()')[0].strip(),
            }
            csv_writer.writerow(data_dic)
    with ExcelWriter('电影票房.xlsx') as f:
        pd.read_csv("电影票房.csv", encoding='utf-8').to_excel(f, sheet_name="电影票房", index=False)


if __name__ == '__main__':
    main()
