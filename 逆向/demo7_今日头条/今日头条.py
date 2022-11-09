import requests
import time
import execjs
from redis import StrictRedis


def get_signature(url):
    with open('头条.js', 'r', encoding='utf-8') as f:
        js = execjs.compile(f.read(), cwd=r'C:\Users\Administrator\AppData\Roaming\npm\node_modules')
        signature = js.call('get_sign', url)
        return signature


def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    session = requests.session()
    session.headers = headers
    url = f"https://www.toutiao.com/api/pc/list/feed?channel_id=3189398972&max_behot_time={int(time.time() * 1000)}&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web"
    signature = get_signature(url)
    new_url = f'{url}&_signature={signature}'

    res = session.get(new_url, headers=headers)
    for data in res.json()['data']:
        video_play_info = data.get('video_play_info')
        if not video_play_info:
            user = data.get('user')
            if user:
                name = user.get('name')
            else:
                name = data.get('user_info').get('name')
            title = data['title']
            url = data['share_url']
            content = data.get('content')
            dic = {
                'user': name,
                'title': title,
                'content': content,
                'url': url,
            }
            conn.sadd('今日头条', str(dic))
            print(name, 'over')
        else:
            video_datas = data.get('data')
            if video_datas:
                for video_data in video_datas:
                    name = video_data.get('user_info').get('name')
                    title = video_data['title']
                    url = video_data['share_url']
                    dic = {
                        'user': name,
                        'title': title,
                        'url': url,
                    }
                    conn.sadd('今日头条_video', str(dic))
                    print(name, 'over')
            else:
                name = data.get('user_info').get('name')
                title = data['title']
                url = data['share_url']
                dic = {
                    'user': name,
                    'title': title,
                    'url': url,
                }
                conn.sadd('今日头条_video', str(dic))
                print(name, 'over')


if __name__ == '__main__':
    conn = StrictRedis(db=1, password='20020224.')

    main()
