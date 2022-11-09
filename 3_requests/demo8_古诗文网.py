import requests

url = 'https://so.gushiwen.cn/user/collect.aspx?type=s'
proxy = {
    'https': 'http://127.0.0.1:7890'
}
headers = {
    'cookie': 'login=flase; ASP.NET_SessionId=skla0p2jx3rukm3mtzroeofg; ticketStr=202339330%7cgQEb8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAycW5XR1JlbGVkN2kxWVc2SHh5MTcAAgQ6OcRiAwQAjScA; codeyzgswso=0c67dcb9527cb94a; gsw2017user=2982285%7c7C72431797D52D79577099D0FA29B272; login=flase; wxopenid=defoaltid; gswZhanghao=18533538210; gswPhone=18533538210',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
session = requests.session()
res = session.get(url=url, headers=headers, proxies=proxy)
print(res.text)
