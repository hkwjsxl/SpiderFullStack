import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
from bs4 import BeautifulSoup


def a(a):
    return 'Chcmd7MmUWBL3J72'


def aes_enc(data, b):
    data = data.encode('utf-8')
    key = b.encode('utf-8')
    iv = b'0102030405060708'
    aes = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    data = pad(data, 16)
    enc_data = aes.encrypt(data)
    return base64.b64encode(enc_data).decode()


def c(a, b, c):
    return '7421d3ee3b3121e77af356e340685399705e6f1a47e62217cc074da675dabe566dda1df3c5116a4d7cde5390dc9490fdecc9f30959fb47a43016fdee6e54f79b12f283cf5c2478712c01232352bea5ac388d3155e4fc1570f819a3a9b57aa2720c6cb09f48a95c3c71b14055686d54da5c19b5880f068d829b527540715e658b'


def asrsea(data, e, f, g):
    i = a(16)
    enc_text = aes_enc(data, g)
    enc_text = aes_enc(enc_text, i)
    enc_sec_key = c(i, e, f)
    return enc_text, enc_sec_key


def get_enc_param(data):
    enc_text, enc_sec_key = asrsea(
        json.dumps(data),
        e='010001',
        f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
        g='0CoJUm6Qyw8W8jud')
    enc_data = {
        'params': enc_text,
        'encSecKey': enc_sec_key,
    }
    return enc_data


def get_song_res(url, song_id):
    data = {
        'encodeType': "aac",
        'ids': [song_id],
        'level': "standard",
        'csrf_token': "e7aa85c531302e3af53c69c8816c6564"
    }
    enc_data = get_enc_param(data)
    res = requests.post(url, data=enc_data, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    return res.json()


def get_detail_res(url):
    detail_data = {
        'csrf_token': "e7aa85c531302e3af53c69c8816c6564",
        'limit': "1000",
        "offset ": " 0",
        'order': "true"
    }
    enc_data = get_enc_param(detail_data)
    detail_res = requests.post(url, data=enc_data, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})
    return detail_res.json()


def parse_index_page(url):
    index_res = requests.get(url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    })
    soup = BeautifulSoup(index_res.text, 'lxml')
    title = soup.find('title').text
    return title


def parse_comment(url, song_id):
    comment_data = {
        'csrf_token': "e7aa85c531302e3af53c69c8816c6564",
        'cursor': "-1",
        'offset': "0",
        'orderType': "1",
        'pageNo': "1",
        'pageSize': "100",  # 评论数
        'rid': f"R_SO_4_{song_id}",
        'threadId': f"R_SO_4_{song_id}",
    }
    enc_data = get_enc_param(comment_data)
    comment_res = requests.post(url, data=enc_data, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    })
    print(comment_res.json())
    return comment_res.json()['data']


def main():
    # song_id = input('请输入歌曲id>>>: ').strip()
    song_id = '475479888'
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1'
    # detail_url = 'https://music.163.com/weapi/user/getfollows/1909556837'
    # detail_res = get_detail_res(detail_url)
    index_url = f'https://music.163.com/song?id={song_id}'
    song_res = get_song_res(url, song_id)
    title = parse_index_page(index_url)
    for song_data in song_res['data']:
        song_url = song_data['url']
        content = requests.get(song_url).content
        with open(f'{title}.mp3', 'wb') as f:
            f.write(content)
        print(title, '下载完成!')

    comment_url = 'https://music.163.com/weapi/comment/resource/comments/get'
    comment_res = parse_comment(comment_url, song_id)
    for comment in comment_res['comments']:
        content = comment['content']
        user_name = comment['user']['nickname']
        user_id = comment['user']['userId']
        time_str = comment['timeStr']
        text = str(user_id) + ', ' + str(user_name) + ', ' + content + time_str +  '\n'
        with open(f'{title}_comment.txt', 'a', encoding='utf-8') as f:
            f.write(text)
    # 热评
    for comment in comment_res.get('hotComments'):
        if comment:
            content = comment['content']
            user_name = comment['user']['nickname']
            user_id = comment['user']['userId']
            time_str = comment['timeStr']
            text = str(user_id) + ', ' + str(user_name) + ', ' + content + time_str + '\n'
            with open(f'{title}_comment_hot.txt', 'a', encoding='utf-8') as f:
                f.write(text)
    print('comment, 下载完成')


if __name__ == '__main__':
    main()
