import os
import re
import aiohttp
import aiofiles
import asyncio


class JJMJ:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        self.proxy = 'http://127.0.0.1:7890'
        self.file_path = '九九美剧'
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)

    async def get_main_m3u8_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, proxy=self.proxy) as res:
                page_source = await res.text()
                m3u8_url = re.findall('"url":"(.*?index.m3u8)",', page_source, re.S)[0].replace('\\', '')
                return m3u8_url

    async def get_m3u8_url_list(self):
        tasks = []
        for i in range(1, 6):
            main_url = f'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-{i}.html'
            tasks.append(asyncio.create_task(self.get_main_m3u8_url(main_url)))
        return await asyncio.gather(*tasks)

    async def get_index_url(self, m3u8_url):
        async with aiohttp.ClientSession() as session:
            async with session.get(m3u8_url, headers=self.headers, proxy=self.proxy) as res:
                page_source = await res.text()
                index_url = page_source.split('\n')[-2]
                index_url = 'https://new.qqaku.com' + index_url
                return index_url

    async def get_all_ts_url(self, index_url, i):
        async with aiohttp.ClientSession() as session:
            async with session.get(index_url, headers=self.headers, proxy=self.proxy) as res:
                page_source = await res.text()
                async with aiofiles.open(f'{self.file_path}/{i}.text', 'w', encoding='utf-8') as f:
                    for line in page_source.split('\n'):
                        ts_url = line.strip()
                        await f.write(ts_url + '\n')
                    print(f'{i}.text---写入完毕!')

    async def download(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for ts_file in os.listdir(self.file_path):
                tasks.append(asyncio.create_task(self.download_one(session, ts_file)))
            await asyncio.wait(tasks)

    async def download_one(self, session, ts_file):
        path = self.file_path + '/' + ts_file.split('.')[0]
        if not os.path.exists(path):
            os.mkdir(path)
        async with aiofiles.open(f'{self.file_path}/{ts_file}', 'r', encoding='utf-8') as f:
            i = 1
            for ts_url in await f.readlines():
                if ts_url.startswith('https'):
                    ts_url = ts_url.strip()
                    while True:
                        try:
                            async with session.get(ts_url) as res:
                                content = await res.content.read()
                                async with aiofiles.open(os.path.join(path, str(i)) + '.ts', 'wb') as f1:
                                    await f1.write(content)
                                i += 1
                                print(ts_url, '下载完成!')
                            break
                        except:
                            print(ts_url, '下载失败!')

    def do_m3u8_url(self, m3u8_filename='index.m3u8'):
        file_name = m3u8_filename.split('.')[0]
        with open(os.path.join(self.file_path, m3u8_filename), mode='r', encoding='utf-8') as f:
            data = f.readlines()
        fw = open(os.path.join(self.file_path, file_name) + '.m3u8', 'w', encoding='utf-8')
        abs_path = os.getcwd()
        i = 1
        for line in data:
            if line.startswith('#'):
                fw.write(line)
            else:
                # 写入本地路径
                fw.write(f'{abs_path}/{self.file_path}/{file_name}/{i}.ts\n')
                i += 1

    def merge(self, index_m3u8, filename):
        src_path = os.getcwd()
        os.chdir(self.file_path)
        cmd = f'ffmpeg -i {index_m3u8} -c copy {filename}.mp4'
        os.system(cmd)
        os.chdir(src_path)

    def run(self):
        loop = asyncio.get_event_loop()
        m3u8_url_list = loop.run_until_complete(self.get_m3u8_url_list())
        i = 1
        for m3u8_url in m3u8_url_list:
            index_url = loop.run_until_complete(self.get_index_url(m3u8_url))
            loop.run_until_complete(self.get_all_ts_url(index_url, i))
            i += 1

        loop.run_until_complete(self.download())

        path = os.listdir(self.file_path)
        for file_name in path:
            if file_name.endswith('text'):
                self.do_m3u8_url(file_name)
                self.merge(file_name.split('.')[0] + '.m3u8', file_name.split('.')[0])


if __name__ == '__main__':
    mj = JJMJ()
    mj.run()
