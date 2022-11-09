import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import ddddocr
import base64
import json

url = 'https://user.wangxiao.cn/login'
session = requests.session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 拿到cookies---session_id
res = session.get(url)

code_url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
code_res = session.post(code_url, headers={'Content-Type': 'application/json;charset=UTF-8'})
img_b64 = code_res.json()['data'].split('base64,')[1]

# 识别验证码
ocr = ddddocr.DdddOcr()
img_bytes = base64.b64decode(img_b64)
code = ocr.classification(img_bytes)

# 拿到getTime---data
get_time_url = 'https://user.wangxiao.cn/apis//common/getTime'
get_time_res = session.post(get_time_url, headers={'Content-Type': 'application/json;charset=UTF-8'})

# password加密
password = 'h20020224.'
enc_params = password + get_time_res.json()['data']
b64_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
b64_bytes = base64.b64decode(b64_key)
key = RSA.import_key(b64_bytes)
enc_key = PKCS1_v1_5.new(key=key)
enc_data = enc_key.encrypt(enc_params.encode('utf-8'))
enc_password = base64.b64encode(enc_data).decode()
login_data = {
    'imageCaptchaCode': code,
    'password': enc_password,
    'userName': "18533538210"
}

login_url = 'https://user.wangxiao.cn/apis//login/passwordLogin'
login_res = session.post(login_url, headers={'Content-Type': 'application/json;charset=UTF-8'},
                         data=json.dumps(login_data))

# js保持设置登录cookies
session.cookies['autoLogin'] = 'true'
session.cookies['userInfo'] = json.dumps(login_res.json()['data'])
session.cookies['token'] = login_res.json()['data']['token']

# $.cookie("UserCookieName", e.userName, n),
# $.cookie("OldUsername2", e.userNameCookies, n),
# $.cookie("OldUsername", e.userNameCookies, n),
# $.cookie("OldPassword", e.passwordCookies, n),
# $.cookie("UserCookieName_", e.userName, n),
# $.cookie("OldUsername2_", e.userNameCookies, n),
# $.cookie("OldUsername_", e.userNameCookies, n),
# $.cookie("OldPassword_", e.passwordCookies, n),
# e.sign && (n.expires = 365,
# $.cookie(e.userName + "_exam", e.sign, n))

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

question_url = 'https://ks.wangxiao.cn/practice/listQuestions'
question_data = {
    "examPointType": "",
    "practiceType": "2",
    "questionType": "",
    "sign": "jz1",
    "subsign": "06b63e70bc689554c433",
    "top": "30"
}
question_res = session.post(question_url, data=json.dumps(question_data),
                            headers={'Content-Type': 'application/json;charset=UTF-8'})
print(question_res.text)



