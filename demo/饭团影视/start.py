import re
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

"""
加密算法:AES
key ： Of84ff0clf252cba
iv  ： c487ebl2e38a0faO
mode : CBC
pad : ZeroPadding
"""


# 针对pad : ZeroPadding
# def AES_Encrypt(data):
#     key = b'Of84ff0clf252cba'
#     iv = b'c487ebl2e38a0faO'
#     pad = lambda s: s + (16 - len(s) % 16) * chr(0)
#     data = pad(data)
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     encryptedbytes = cipher.encrypt(data.encode('utf8'))
#     encodestrs = base64.b64encode(encryptedbytes)
#     enctext = encodestrs.decode('utf8')
#     return enctext

def AES_Decrypt(data):
    key = b'Of84ff0clf252cba'
    iv = b'c487ebl2e38a0faO'
    enc_bytes = base64.decodebytes(data.encode('utf-8'))
    aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    text_dec = aes.decrypt(enc_bytes)
    unpad_data = unpad(text_dec, 16)
    dec_data = unpad_data.decode('utf-8')
    return dec_data


def get_url():
    main_url = 'https://www.fantuanhd.com/play/id-1177-1-1.html'
    session.headers.update({
        'referer': 'https://www.fantuanhd.com/',
    })
    res = session.get(main_url, headers=session.headers)
    url = re.search(r'"url":"(?P<url>.*?)","url_next"', res.text).group('url')
    return url


def get_urls(url):
    enc_urls = 'https://dp.1010dy.cc/'
    params = {
        'url': url,
        'next': '',
        'id': '1177',
        'nid': '1',
        'from': 'uploadixigua',
    }
    res = session.get(enc_urls, headers=session.headers, params=params)
    urls = re.search(r'var urls = "(?P<urls>.*?)";', res.text).group('urls')
    return urls


def down_video(video_url):
    print('url解密成功', video_url)
    refer_sign = re.search(r'https://(?P<sign>.*).douyinvod.com/', video_url).group('sign')
    print(refer_sign)
    headers = {
        'referer': f'https://{refer_sign}.douyinvod.com',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    content = session.get(video_url, headers=headers).content
    print('正在下载---')
    print(content)
    with open('video_url.mp4', mode='wb') as f:
        f.write(content)
    print('下载成功---')


def main():
    url = get_url()
    print(url)
    urls = get_urls(url)
    print(urls)
    video_url = AES_Decrypt(urls)
    print(video_url)
    down_video(video_url)


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    main()

