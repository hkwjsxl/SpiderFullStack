import time
import requests
import base64
from hashlib import sha1


def enc_sha1(e):
    sha1_obj = sha1()
    sha1_obj.update(e.encode('utf-8'))
    return sha1_obj.hexdigest()


def enc_base64(e):
    return base64.b64encode(e).decode()


def get_token(*args):
    t = str(int(time.time()))
    r = []
    n = 0
    if n < len(args):
        r.append(args[n])
        n += 1
    r.append(t)
    o = enc_sha1(','.join(r))
    s = enc_base64((o + ',' + t).encode('utf-8'))
    return s


def main():
    url = 'https://antispider8.scrape.center/api/movie/'
    token = get_token("/api/movie")
    print(token)
    params = {
        'limit': '10',
        'offset': '0',
        'token': token,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    res = requests.get(url, params=params, headers=headers)
    print(res.json())


if __name__ == '__main__':
    main()
