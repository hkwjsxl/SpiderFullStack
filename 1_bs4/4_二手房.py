from bs4 import BeautifulSoup


soup = BeautifulSoup(open('广州二手房.html', encoding='utf-8'), 'lxml')
# print(soup.title.text)
for item in soup.select('.house-title a'):
    print(item['title'], item['href'])


