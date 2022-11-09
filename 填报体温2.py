import requests
from lxml import etree
from urllib.parse import urljoin
import ddddocr
import binascii


def get_csrf_and_code():
    url = 'https://ksxskj.hevttc.edu.cn'
    res = session.get(url, headers=session.headers, verify=False)
    tree = etree.HTML(res.text)
    code_path = tree.xpath('//img[@id="valid-img"]/@src')[0]
    code_url = urljoin(url, code_path)
    code_res = session.get(code_url, headers=session.headers).content
    with open('code.png', 'wb') as f:
        f.write(code_res)
    ocr = ddddocr.DdddOcr()
    with open("code.png", 'rb') as f:
        image = f.read()
    code = ocr.classification(image)
    return session.cookies.get('csrftoken'), code


def login(csrf, code, username='', password=''):
    url = 'https://ksxskj.hevttc.edu.cn/login/?next=/'
    session.headers.update({
        'Referer': 'https://ksxskj.hevttc.edu.cn/login/?next=/',
    })
    next_value = '%' + binascii.b2a_hex('/'.encode('utf-8')).decode()
    data = {
        'csrfmiddlewaretoken': csrf,
        'username': username,
        'password': password,
        'check_code': code,
        'next': next_value,
    }
    session.post(url, headers=session.headers, data=data)
    return session.cookies.get('csrftoken')


def main():
    while True:
        username = input('请输入学号：').strip()
        password = input('请输入密码：').strip()
        if not username or not password:
            print('请输入正确的参数!')
            continue
        break
    addr = input('请输入地址（河北省 邯郸市 临漳县 [默认]）：').strip() or '河北省 邯郸市 临漳县'
    csrf, code = get_csrf_and_code()
    csrf = login(csrf, code, username, password)
    am_url = 'https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/ambt/'
    pm_url = 'https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/pmbt/'
    session.headers.update({
        'Referer': 'https://ksxskj.hevttc.edu.cn/person_dir/',
    })
    data = {
        'csrfmiddlewaretoken': csrf,
        'tw': '36.4',
        'fl': 'False',
        'gk': 'False',
        'hx': 'False',
        'qt': 'False',
        'jc': 'False',
        'fx': 'False',
        'jqjc': '',
        'lc': addr,
        'actionName': 'actionValue',
    }
    am_res = session.post(am_url, headers=session.headers, data=data)
    print(am_res.text)
    print(''.center(50, '-'))
    pm_res = session.post(pm_url, headers=session.headers, data=data)
    print(pm_res.text)
    print('over'.center(50, '-'))
    input('---任意键退出---')


if __name__ == '__main__':
    session = requests.session()
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102K1AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/5979 MicroMessenger/8.0.27.2220(0x28001B3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxb8b3f96e091ed96e'
    }
    main()

