import requests


def main():
    url = 'https://www.cdt-ec.com/gwmanage/pub/notices'
    params = {
        'appcode': 'datang',
        'pageIndex': '1',
        'pageSize': '100',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers, params=params)
    print(res.text)


if __name__ == '__main__':
    main()

