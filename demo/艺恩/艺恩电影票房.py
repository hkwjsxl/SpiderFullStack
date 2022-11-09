import requests
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import binascii
import json


def dec_des(key, enc_data):
    des = DES.new(key=key, mode=DES.MODE_ECB)
    result = des.decrypt(enc_data)
    result = unpad(result, 8)
    return result.decode('utf-8')


def func1(a, b, c):
    if b == 0:
        return a[c:]
    d = str(a[:b])
    d += a[b + c:]
    return d


def dec_data(data):
    len(data) - 1
    a = int(data[len(data) - 1], 16) + 9
    b = int(str(data[a]), 16)
    data = func1(data, a, 1)
    a = data[b: b + 8]
    data = func1(data, b, 8)
    b = a.encode('utf-8')
    a = a.encode('utf-8')
    a = dec_des(b, binascii.a2b_hex(data))
    return a


def main():
    url = 'https://www.endata.com.cn/API/GetData.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    data = {
        'year': '2022',
        'MethodName': 'BoxOffice_GetYearInfoData'
    }
    res = requests.post(url, headers=headers, data=data)
    dec_result = dec_data(res.text)
    r_index = dec_result.rindex('}')
    result = json.loads(dec_result[:r_index + 1])
    print(result)


if __name__ == '__main__':
    main()
