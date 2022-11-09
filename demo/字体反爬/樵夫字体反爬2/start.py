import requests
import re
import os
from urllib.parse import urljoin
from fontTools.ttLib import TTFont
from PIL import Image, ImageFont, ImageDraw
from lxml import etree
import pytesseract


def down_font():
    url = 'http://bikongge.com/chapter_1/font_2/index.html'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    font_face = re.search(r'@font-face {.*?font-family: "shit-font";(?P<font_face>.*?)}', res.text, re.S)
    if not font_face:
        raise ValueError('font_face空值!')
    font_url = re.search(', url\("(?P<font_url>.*?)"\);', font_face.group('font_face'), re.S)
    if not font_url:
        raise ValueError('font_url空值!')
    font_url = urljoin(url, font_url.group('font_url'))
    font_res = requests.get(font_url, headers=headers)
    font_name = os.path.split(font_url)[1]
    with open(font_name, 'wb') as f:
        f.write(font_res.content)
    return font_name


def handle_font(font_name):
    font_obj = TTFont(font_name)
    font_list = [i.replace('uni', r'\u') for i in font_obj.getGlyphOrder()[2:]]
    print(font_list)
    print(len(font_list))

    img_obj = Image.new('RGB', (300, 200), (255, 255, 255))
    img_draw = ImageDraw.Draw(img_obj)
    img_font = ImageFont.truetype(font_name, 30)
    for i in range(len(font_list)):
        uni = font_list[i].encode('utf-8').decode('unicode-escape')
        img_draw.text((20 + 20 * i, 20), uni, 1, img_font)
    img_obj.save('result.png', format='png')

    ocr_result = pytesseract.image_to_string('result.png').strip()
    print(ocr_result)
    print(len(ocr_result))
    if len(ocr_result) != len(font_list):
        raise ValueError('长度不一!')

    map_dic = dict(zip(font_list, ocr_result))
    print(map_dic)
    return map_dic


def handle_html(map_dic):
    url = 'http://bikongge.com/chapter_1/font_2/index.html'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    page_source = res.text
    for k, v in map_dic.items():
        kk = k.replace(r'\u', '&#x') + ';'
        kk = kk.lower()
        page_source = page_source.replace(kk, v)
    return page_source


def parse_html(page_source):
    tree = etree.HTML(page_source)
    info_list = tree.xpath('//div[@class="board-item-content"]')
    for info in info_list:
        title = info.xpath('./div[@class="movie-item-info"]/p/a/text()')[0]
        star = info.xpath('./div[@class="movie-item-info"]/p[@class="star"]/text()')[0].replace('主演：', '')
        create_time = info.xpath('./div[@class="movie-item-info"]/p[@class="releasetime"]/text()')[0] \
            .replace('上映时间：', '')
        piaofang_realtime = info.xpath(
            './div[@class="movie-item-number boxoffice"]/p[@class="realtime"]//span[@class="stonefont"]/text()')[0]
        piaofang_total = info.xpath(
            './div[@class="movie-item-number boxoffice"]/p[@class="total-boxoffice"]//span[@class="stonefont"]/text()') \
        [0]
        data_dict = {
            '标题': title,
            '主演': star,
            '上映时间': create_time,
            '实时票房(万)': piaofang_realtime,
            '总票房(亿)': piaofang_total,
        }
        print(data_dict)


def main():
    # font_name = down_font()
    map_dic = handle_font('d1a7c1ff.woff')
    page_source = handle_html(map_dic)
    parse_html(page_source)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    main()
