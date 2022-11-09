# """
# 1.想办法拿到字体文件
# 2.对字体文件进行解析.
#     unicode -> 正确的文字 (难)
# 3.在获取到页面源代码后.
# 把unicode中的文字进行替换. 后续就可以正常处理了
# """
#
# # 1.获取到字体文件
import requests
from lxml import etree
# from urllib.parse import urljoin
# import re
#
# # 我的网站. 本案例不用给ua
# url = "http://bikongge.com/chapter_1/font_1/index.html"
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# # print(resp.text)
#
# # 获取style.css
# tree = etree.HTML(resp.text)
# href = tree.xpath("//link/@href")[0]
# href = urljoin(url, href)
# # print(href)
#
# font_resp = requests.get(href)
# font_url_re = re.compile(r'src: url\("(?P<font_url>.*?)"\);', re.S)
# font_url = font_url_re.search(font_resp.text).group("font_url")
# # print(font_url)
#
# # url拼接
# # 这个url应该和谁拼接
# font_url = urljoin(href, font_url)
# print(font_url)
#
# font_resp = requests.get(font_url)
# with open("font.woff", mode="wb") as f:
#     f.write(font_resp.content)
#
# # font-creator可以打开字体文件(只有windows), 可以不装的.
# s = "\ue0df"  # unicode  
# print(s)
# # font-creator里看到的是 \ue0df => 店(字体文件)
# # 照着字体文件里面的样子. 把所有的字形画出来, 画到图片上去.
# # 然后用AI_OCR去识别这个图片. 就知道了该字形对应的文字是什么.
# # 这个unicode对应的正确文字是什么

# 需要font-tools来获取到unicode
# pip install fontTools
from fontTools.ttLib import ttFont

ttf = ttFont.TTFont("ae0f8407.woff")
uni_list = ttf.getGlyphOrder()[2:]  # 推荐使用, 有顺序

uni_ok_list = []
for uni in uni_list:
    uni = uni.replace("uni", "\\u")
    uni_ok_list.append(uni)
print(uni_ok_list)
print(len(uni_ok_list))

# 按照字体文件里的字形. 把上述unicode画出来.
# 安装 pip install pillow
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# 创建图片
img = Image.new("RGB", (1800, 1000), color=(255, 255, 255))

# 准备一只可以在图上画画的笔
img_draw = ImageDraw.Draw(img)

# 准备好画图的字体
img_font = ImageFont.truetype("ae0f8407.woff", 40)

# 准备文字
# 一行40个字
#  9条数据
# 索引号. 如果 索引%4 == 0 是不是该换行了?
# 行号: 索引 // 4 + 1

line_length = 43  # 无法固定.

new_line = []
for i in range(len(uni_ok_list)):
    # 把\\uxxxx修改成unicode码
    uni = uni_ok_list[i]
    # 需要用编码的转换来进行调整
    uni = uni.encode().decode("unicode-escape")
    if i % line_length == 0 and i != 0:
        # 该换行了 写入该行
        new_line_s = "".join(new_line)
        # 可以画到图片了
        img_draw.text((20, (i // line_length + 1) * line_length), new_line_s, fill=1, font=img_font)
        new_line = [uni]  # 该行写完. 准备写下一行.
    else:
        # 正常该行内的内容
        new_line.append(uni)

if new_line:
    new_line_s = "".join(new_line)
    # 可以画到图片了
    img_draw.text((20, (len(uni_ok_list) // line_length + 2) * line_length), new_line_s, fill=1, font=img_font)

# 完成上述操作. 你只是在内存中画了一张图.
# 保存到硬盘上
img.save("tu.jpg")


# 接下来就是识别上面这张图.
# 获取到所有文字.
# 文字识别。 没有百分之百的准确率。
# 1. ddddocr
# 2. Tesseract-OCR
# 3. 火山（字节）
# 4. 百度AI(比上面这几个都好一些)

from aip import AipOcr

"""刚才创建的那个应用里. 有下面这三个东西"""
APP_ID = '27643903'
API_KEY = 'atSZosOQ1xOQmBOmGSgLnbNA'
SECRET_KEY = 'znj959V9ZN0zlGVhZexABFT4ek57Kom2'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

f = open("tu.jpg", mode="rb")
r = client.basicGeneral(f.read())

result_list = []
for item in r['words_result']:
    result_list.extend(item['words'])
    print(item['words'])
print(len(result_list))
# 吧unicde对应的word进行映射 -> 字典
# zip有水桶效应, 在本案例中. uni_ok_list和result_list必须长度保持一致.
dic = dict(zip(uni_ok_list, result_list))
print(dic)
# {"\\uxxxx": 天}

# 替换
# 获取页面源代码.
# # 我的网站. 本案例不用给ua
url = "http://bikongge.com/chapter_1/font_1/index.html"
resp = requests.get(url)
resp.encoding = 'utf-8'

page_source = resp.text

for k in dic:
    # k: \\uxxxxx
    # v: 天
    v = dic[k]

    kk = k.replace("\\u", "&#x") + ";"
    # 字符串不可变. 需要重新赋值
    page_source = page_source.replace(kk, v)

print(page_source)
