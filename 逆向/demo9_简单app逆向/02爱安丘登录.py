import requests
import random
import string


def get_code():
    url = 'https://app-auth.iqilu.com/member/phone/code'
    imei = str(''.join(random.choices(string.digits + 'abcdef', k=16)))
    session.cookies.update({
        'orgid': '137',
    })
    session.headers.update({
        'orgid': '137',
        'cq-agent': '{"os":"android","imei":%s,"osversion":"12","network":"wifi","version":"0.0.35.1007","core":"1.7.4","brand":"Xiaomi"}' % imei,
    })
    data = {
        "phone": "18533538213",
        "senderName": "aliyun",
        "tokenCode": "RXt1dZ4T6tplh4MbzbXuHnsYNf/O9286gRX+OJQuZIHDiyOfg9ISjnBXMraKHl1Ou2Hs3A+z/7cMA7oMcj5gDQ=="
    }
    res = session.post(url, headers=session.headers, json=data, verify=False)
    print(res.text)


def main():
    get_code()
    url = 'https://app-auth.iqilu.com/member/login'

    data = {
        "phone": "18533538210",
        "code": "132130",
        "key": "",
        "captcha": "",
        "captchaKey": ""
    }
    # res = requests.post(url, headers=session.headers, json=data)
    # print(res.text)


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'user-agent': 'chuangqi.o.137.com.iqilu.app137/0.0.35.1007'
    }
    main()
