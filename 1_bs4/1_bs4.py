import re
from bs4 import BeautifulSoup

html_data = """
<html lang="en">
<head>
    <title>
        The Dormouse's story
    </title>
</head>
<body>
<p class="title">
    <b>
        The Dormouse's story
    </b>
</p>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a class="sister" href="http://example.com/elsie" id="link1">
        Elsie
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
    </a>
    and
    <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
    </a>
    and they lived at the bottom of a well.
</p>
<p class="story">
    this is a story
</p>
</body>
</html>
"""
# html_data = '<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>'
soup = BeautifulSoup(html_data, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.text)

# print(soup.title.parent)
# print(soup.title.parent.name)

# print(soup.a['class'])
# print(soup.find(id='link1'))
# print(soup.find('a', id='link1'))
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all('a', attrs={'id': 'link2'}))
# print(soup.find('a', attrs={'class': 'sister'}))
# print(soup.find_all('a', attrs={'class': 'sister'}))

# print(soup.get_text())

# print(soup.a.string)  # 可以拿到注释
# print(type(soup.a.string))  # <class 'bs4.element.NavigableString'>
# print(type(soup.a))  # <class 'bs4.element.Tag'>
# print(type(soup.a.name))  # <class 'str'>
# print(type(soup.b.text))  # <class 'str'>

# print(soup.title.contents)  # 返回列表，["\n        The Dormouse's story\n    "]
# print(soup.title.contents[0].strip())  # The Dormouse's story

# 字符串没有 `.contents` 属性,因为字符串没有子节点:
# print(soup.title.contents[0].contents)  # AttributeError: 'NavigableString' object has no attribute 'contents'

# print(list(soup.title.children))
# print(list(soup.find('p').children))
# === print(list(soup.p.children))
# print(list(soup.find_all('p').children))  # 报错

# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

# print(list(soup.p.children))
# print(list(soup.p.descendants))

# print(soup.a.text)  # 区别：text返回内容为字符串类型  strings, stripped_strings为生成器generator
# print(list(soup.a.strings))  # ['\n        Elsie\n    ']
# print(list(soup.a.stripped_strings))  # ['Elsie']
# print(list(soup.title.stripped_strings))  # `.stripped_strings` 可以去除多余空白内容

# print(type(soup.html))  # <class 'bs4.element.Tag'>
# print(type(soup.html.parent))  # <class 'bs4.BeautifulSoup'>

# print(soup.find_all(string=re.compile('sisters')))  # # 模糊查询 包含sisters的就可以

# print(soup.find_all(['a', 'b']))  # 所有的a标签和b标签

# print(soup.find_all(href=re.compile('elsie')))
# print(soup.find_all(text=re.compile("The")))
# print(soup.find_all(class_=re.compile("story")))

# print(soup.find_all(id=True))  # 含有id属性的
# print(soup.find_all(class_='title'))  # class属性为title的

# print(soup.find_all("a", limit=2))  # 只要两条
# print(soup.find_all("a")[0:2])

# print(soup.head.title)
# print(soup.find("head").find("title"))

# print(list(soup.a.find_parent()))
# print(list(soup.a.find_parents()))
# print(list(soup.a.find_parents('p')))

# print(soup.select('a'))
# print(soup.select('.sister'))
# print(soup.select('#link1'))
# print(soup.select('p .sister'))
# print(soup.select('p .sister#link2'))
# print(soup.select('a[href="http://example.com/tillie"]'))

