import requests
import subprocess
from functools import partial


subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')


if __name__ == '__main__':
    # execjs 必须放后面
    import execjs

    url = 'https://www.endata.com.cn/API/GetData.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    data = {
        'year': '2016',
        'MethodName': 'BoxOffice_GetYearInfoData',
    }
    res = requests.post(url, headers=headers, data=data)
    f = open('艺恩js2.js', mode='r', encoding='utf-8')
    js = execjs.compile(f.read())
    data = js.call('exec', res.text)
    print(data)



