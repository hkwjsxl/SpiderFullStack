import requests


def main():
    url = 'http://cd.tibetairlines.com.cn:9100/login'
    headers = {
        'User-Agent': 'android_system_webview'
    }
    data = {
        'grant_type': 'password',
        'isLogin': 'true',
        'password': '123456789',
        'username': '562172420,F',
    }
    res = requests.post(url, headers=headers, data=data)
    print(res.text)


if __name__ == '__main__':
    main()
