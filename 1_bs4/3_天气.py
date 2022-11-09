from bs4 import BeautifulSoup

soup = BeautifulSoup(open('匹配天气.html', encoding='utf-8'), 'lxml')
print(soup.title.text)
for item in soup.select('.w_city.city_guonei'):
    print(item.text)
