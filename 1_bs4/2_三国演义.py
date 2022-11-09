from bs4 import BeautifulSoup

soup = BeautifulSoup(open('../2_xpath/三国演义.html', encoding='utf-8'), 'lxml')
# print(soup.title.text)
for item in soup.select('.book-mulu a'):
    print(item.text)
