import requests
import re
import pandas as pd


def save_data(data_dict):
    df = pd.DataFrame(data_dict)
    df.to_csv('danmu.csv', mode='a', encoding='utf-8-sig')
    print(f'\033[1;33m{df}\033[1;31m')

    print('"over"'.center(50, '-'))


if __name__ == '__main__':

    headers = {
        'cookie': '_uuid=17D39D2A-A21E-8043-92AD-B1B6F2AF4EC320579infoc; buvid3=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; buvid_fp_plain=06201A74-4D4D-4BFD-B069-FED89C254CB9148826infoc; SESSDATA=ba30c108%2C1651584260%2C8b69f%2Ab1; bili_jct=bde1afe7475a50bf6dc17fafafa2f303; DedeUserID=506963849; DedeUserID__ckMd5=6bbdace67271ad46; sid=jwmr0br2; blackside_state=1; rpdid=|(JYl)kkk)mR0J\'uYJY|JJu~u; LIVE_BUVID=AUTO5616362112472401; PVID=1; video_page_version=v_old_home; i-wanna-go-back=-1; b_ut=5; fingerprint3=39df0467a8ac842fbec247cd80b4a3a2; fingerprint=12d37e45743125341a6784d0c9a199c4; fingerprint_s=0a74d2020f65156ad539465b08013659; CURRENT_QUALITY=120; CURRENT_BLACKGAP=0; bp_video_offset_506963849=633345459612549100; CURRENT_FNVAL=4048; innersign=1',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/video/BV1Zk4y197QB?from=search&seid=547474017618517557&spm_id_from=333.337.0.0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }

    oid = '174997516'
    # 生成时间序列
    start = '20220220'
    end = '20220303'
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    for date_lst in date_list:
        req = requests.get(f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={oid}&date={date_lst}',
                           headers=headers).text

        # pprint.pprint(req)
        contents = re.findall(':(.*?)@', req)

        # 取出所有汉字
        # contents_list = []
        # for con in contents:
        #     contents_str = re.sub(
        #         r'[^\u4e00-\u9fa5]',
        #         '', str(con))
        #     if contents_str != '':
        #         contents_list.append(contents_str)

        print(f'\033[1;35m{date_lst}\033[0m')
        data_dict = {"contents": contents}
        # save_data(data_dict)