import requests
import ddddocr
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
# 此案例要用PKCS1_v1_5，   PKCS1_OAEP不适用
import base64
import json


def get_code():
    login_page_url = 'https://user.wangxiao.cn/login'
    session.get(login_page_url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    })
    code_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
    res = session.post(code_url, headers=session.headers)
    png_data = res.json()['data'].split('base64,')[1]
    ocr = ddddocr.DdddOcr()
    code = ocr.classification(png_data)
    return code


def enc_pwd(pwd, ress_data):
    pub_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB'
    pub_key = base64.b64decode(pub_key)
    key = RSA.import_key(pub_key)
    rsa = PKCS1_v1_5.new(key=key)
    enc_data = pwd + ress_data
    result = rsa.encrypt(enc_data.encode('utf-8'))
    return base64.b64encode(result).decode()


def login(code):
    gettime_url = 'https://user.wangxiao.cn/apis//common/getTime'
    res = session.post(gettime_url, headers=session.headers)
    login_url = 'https://user.wangxiao.cn/apis//login/passwordLogin'
    password = 'h20020224.'
    enc_password = enc_pwd(password, res.json()['data'])
    data = {
        'imageCaptchaCode': code,
        'password': enc_password,
        'userName': "18533538210",
    }
    login_res = session.post(login_url, headers=session.headers, data=json.dumps(data))
    print(login_res.json())

    """set_cookies"""
    e = login_res.json()['data']
    session.cookies['UserCookieName'] = e['userName']
    session.cookies['OldUsername2'] = e['userNameCookies']
    session.cookies['OldUsername'] = e['userNameCookies']
    session.cookies['OldPassword'] = e['passwordCookies']
    session.cookies['UserCookieName_'] = e['userName']
    session.cookies['OldUsername2_'] = e['userNameCookies']
    session.cookies['OldUsername_'] = e['userNameCookies']
    session.cookies['OldPassword_'] = e['passwordCookies']
    session.cookies[e['userName'] + '_exam'] = e['sign']

    # # test_login
    # question_url = 'https://ks.wangxiao.cn/practice/listQuestions'
    # question_data = {
    #     "examPointType": "",
    #     "practiceType": "2",
    #     "questionType": "",
    #     "sign": "jz1",
    #     "subsign": "06b63e70bc689554c433",
    #     "top": "30"
    # }
    # question_res = session.post(question_url, data=json.dumps(question_data),
    #                             headers={'Content-Type': 'application/json;charset=UTF-8'})
    # print(question_res.json())


def main():
    code = get_code()
    print(code)
    login(code)


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    main()
