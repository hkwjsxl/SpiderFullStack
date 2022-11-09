import base64

import requests
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def login_prev():
    login_prev_url = 'https://catfront.dianping.com/api/pv'
    data = {
        "v": "1",
        "project": "mt-login-component",
        "pageurl": "passport.meituan.com/useraccount/login",
        "timestamp": int(time.time() * 1000)
    }
    res = session.post(login_prev_url, headers=session.headers, data=data)
    print(res.text)


def get_uuid():
    url = 'https://portal-portm.meituan.com/weapp/loginsdk/api/uuid'
    res = session.get(url, headers=session.headers)
    return res.text


def enc_pwd(pwd):
    pub_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCRD8YahHualjGxPMzeIWnAqVGMIrWrrkr5L7gw+5XT55iIuYXZYLaUFMTOD9iSyfKlL9mvD3ReUX6Lieph3ajJAPPGEuSHwoj5PN1UiQXK3wzAPKcpwrrA2V4Agu1/RZsyIuzboXgcPexyUYxYUTJH48DeYBGJe2GrYtsmzuIu6QIDAQAB'
    pub_key = base64.b64decode(pub_key)
    key = RSA.import_key(pub_key)
    rea = PKCS1_v1_5.new(key=key)
    enc_passowrd = rea.encrypt(pwd.encode('utf-8'))
    return base64.b64encode(enc_passowrd).decode()


def login():
    login_prev()
    _uuid = get_uuid()

    token_id = 'bLXIM8oUne7_ngRHe6E4PQ'
    sdkType = 'h5'
    risk_app = '-1'
    risk_platform = '1'
    risk_partner = '-1'
    login_url = f'https://passport.meituan.com/api/v7/account/login?uuid={_uuid}&token_id={token_id}&sdkType={sdkType}&risk_app={risk_app}&risk_platform={risk_platform}&risk_partner={risk_partner}'
    enc_password = enc_pwd('20020224.')
    print(enc_password)
    data = {
        "userTicket": "",
        "requestCode": "",
        "responseCode": "",
        "email": "18533538210",
        "countryCode": "86",
        "h5Fingerprint": "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",
        "setCookie": "true",
        "isMobile": "false",
        "device_name": "",
        "device_type": "Chrome浏览器",
        "device_os": "",
        "pwd": enc_password,
    }
    res = session.post(login_url, headers=session.headers, data=data)
    print(res.text)

def main():
    login()


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    main()
