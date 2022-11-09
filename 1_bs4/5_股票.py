from bs4 import BeautifulSoup


soup = BeautifulSoup(open('股票.html', encoding='gbk'), 'lxml')
print(soup.title.text)
for item in soup.select('#datalist td'):
    print(item.text)



