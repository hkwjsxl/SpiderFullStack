import time
import requests
import os
from concurrent.futures import ThreadPoolExecutor, wait

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
}
proxy = {
    'https': 'http://127.0.0.1:7890'
}


def down_video(url, i):
    resp = requests.get(url, headers=headers, proxies=proxy)
    with open(os.path.join(path, str(i) + '.ts'), mode="wb") as f3:
        f3.write(resp.content)
    print('{} 下载完成！'.format(url))


def download_all_videos(url, path):
    # 请求m3u8文件进行下载
    resp = requests.get(url, headers=headers, proxies=proxy)
    with open("first.m3u8", mode="w", encoding="utf-8") as f:
        f.write(resp.text)
    if not os.path.exists(path):
        os.mkdir(path)
    # 开启线程 准备下载
    pool = ThreadPoolExecutor(max_workers=50)
    # 1. 读取文件
    tasks = []
    i = 0
    with open("first.m3u8", mode="r", encoding="utf-8") as f:
        for line in f:
            # 如果不是url 则走下次循环
            if line.startswith("#"):
                continue
            print(line, i)
            # 开启线程
            tasks.append(pool.submit(down_video, line.strip(), i))
            i += 1
    print(i)
    # 统一等待
    wait(tasks)


# 处理m3u8文件中的url问题
def do_m3u8_url(path, m3u8_filename="first.m3u8"):
    # 这里还没处理key的问题
    if not os.path.exists(path):
        os.mkdir(path)
    # else:
    # shutil.rmtree(path)
    # os.mkdir(path)
    with open(m3u8_filename, mode="r", encoding="utf-8") as f:
        data = f.readlines()

    fw = open(os.path.join(path, m3u8_filename), 'w', encoding="utf-8")
    abs_path = os.getcwd()
    i = 0
    for line in data:
        # 如果不是url 则走下次循环
        if line.startswith("#"):
            # 判断处理是存在需要秘钥
            fw.write(line)
        else:
            fw.write(f'{abs_path}/{path}/{i}.ts\n')
            i += 1


def merge(filePath, filename='output'):
    os.chdir(path)
    cmd = f'ffmpeg -i first.m3u8 -c copy {filename}.mp4'
    os.system(cmd)


if __name__ == '__main__':
    path = 'ts'
    url = 'https://new.qqaku.com/20211124/nLwncbZW/1100kb/hls/index.m3u8'
    # 下载m3u8文件以及ts文件
    # download_all_videos(url, path)
    do_m3u8_url(path)
    # 文件合并
    merge(path)
    print('over')
