import requests
import re
import os
from urllib.parse import urljoin
from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont
import pytesseract
from aip import AipOcr
from lxml import etree


def down_font():
    url = 'http://bikongge.com/chapter_1/font_1/index.html'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    css_path = re.search('<link rel="stylesheet" type="text/css" href="(?P<css_path>.*?)">', res.text, re.S)
    if not css_path:
        raise OSError('没有找到CSS路径!')
    css_path = css_path.group('css_path')
    css_path = urljoin(url, css_path)
    res_css = requests.get(css_path, headers=headers)
    font_path = re.search('src: url\("(?P<font_path>.*?)"\);', res_css.text, re.S)
    if not font_path:
        raise OSError('没有找到font路径!')
    font_path = font_path.group('font_path')
    font_path = urljoin(css_path, font_path)
    font_res = requests.get(font_path, headers=headers)
    font_name = os.path.split(font_path)[1]
    with open(font_name, 'wb') as f:
        f.write(font_res.content)
    return font_name


def handle_font(font_name):
    font = TTFont(font_name)
    # font.saveXML(font_name.split('.')[0] + '.xml')
    font_list = font.getGlyphOrder()[2:]
    font_new_list = [i.replace('uni', r'\u') for i in font_list]
    # print(font_new_list)
    print(len(font_new_list))

    font_size = 40
    row_num = 43
    img_obj = Image.new('RGB', (2000, 1200), (255, 255, 255))
    img_draw = ImageDraw.Draw(img_obj)
    img_font = ImageFont.truetype(font_name, font_size)
    content_list = []
    for i in range(len(font_new_list)):
        uni = font_new_list[i]
        uni = uni.encode('utf-8').decode('unicode-escape')
        if i % row_num == 0 and i != 0:
            content = ''.join(content_list)
            img_draw.text((font_size, (i // row_num + 1) * (font_size + 20)), content, 1, img_font)
            content_list = [uni]  # 注意
        else:
            content_list.append(uni)
    else:
        if content_list:
            content = ''.join(content_list)
            img_draw.text((font_size, (len(font_new_list) // row_num + 2) * (font_size + 20)), content, 1, img_font)
    img_obj.save('img.png', format='PNG')

    # result = pytesseract.image_to_string('img.png', lang='chi_sim')
    # result = result.replace(' ','')
    # print(result)
    # print(len(result))

    """百度AI"""
    APP_ID = '27751139'
    API_KEY = 'kI9mTb6OhcW0ntr1TxEMdiRx'
    SECRET_KEY = 'C8UoFUSMQseQiRszqqPBkvBT0XjtGaz1'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open('img.png', 'rb') as f:
        img_content = f.read()
    result = client.basicGeneral(img_content)
    res_list = []
    for res in result['words_result']:
        res_list.extend(res['words'])
        print(res['words'])
    print(len(res_list))
    if len(res_list) != len(font_new_list):
        raise ValueError('识别数量不准确！')

    """替换字体"""
    url = 'http://bikongge.com/chapter_1/font_1/index.html'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    page_source = res.text
    map_dic = dict(zip(font_new_list, res_list))
    # print(map_dic)
    for k, v in map_dic.items():
        kk = k.replace(r'\u', '&#x') + ';'
        # print(kk)
        page_source = page_source.replace(kk, v)
    # print(page_source)
    return page_source


def parse_html(page_source):
    tree = etree.HTML(page_source)
    big_list = tree.xpath('//div[@class="wrapper"]/div[@class="wrapper-item"]')
    for li in big_list:
        content = li.xpath('.//text()')
        content = ''.join(content).replace(' ', '').replace('\r\n', '')
        print(content)


def main():
    # font_name = down_font(font_name)
    page_source = handle_font('ae0f8407.woff')
    parse_html(page_source)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    main()
