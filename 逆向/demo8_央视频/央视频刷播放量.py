import binascii
import json
import requests
import execjs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time
from concurrent.futures.thread import ThreadPoolExecutor


def get_guid_pid():
    body = """
    function PID() {
        return `${(new Date).getTime().toString(36)}_${Math.random().toString(36).replace(/^0./, "")}`
    }
    function GUID() {
        var t = (new Date).getTime().toString(36)
        var r = Math.random().toString(36).replace(/^0./, "");
        return "".concat(t, "_").concat(r);
    }
    """
    js = execjs.compile(body)
    pid = js.call('PID')
    guid = js.call('GUID')
    return guid, pid


def aes_enc(wn):
    key = "4E2918885FD98109869D14E0231A0BF4"
    iv = "16B17E519DDD0CE5B79D7A63A4DD801C"
    key = binascii.a2b_hex(key)
    iv = binascii.a2b_hex(iv)
    aes = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)
    wn = pad(wn.encode('utf-8'), 16)
    enc = aes.encrypt(wn)
    return "--01" + binascii.b2a_hex(enc).decode().upper()


def get_ckey(vid, guid):
    body = """
    function f(Vn) {
        var Yn = 0;
        var Ne = -5516;
        var Xn;
        for (Mr = 0; Mr < Vn["length"]; Mr++){
            Xn = Vn["charCodeAt"](Mr),
            Yn = (Yn << Ne + 1360 + 9081 - 4920) - Yn + Xn,
            Yn &= Yn;
        }
        return Yn
    }
    """
    platform = "4330701"
    app_ver = "1.2.10"
    ctime = str(int(time.time()))
    ending = "https://w.yangshipin.cn/|mozilla/5.0 (windows nt ||Mozilla|Netscape|Win32|"
    vn = f"|{vid}|{ctime}|mg3c3b04ba|{app_ver}|{guid}|{platform}|{ending}"
    js = execjs.compile(body)
    yn = js.call('f', vn)
    wn = f'|{yn}{vn}'
    return aes_enc(wn)


def get_vurl(vid, guid, pid):
    v_url = 'https://playvv.yangshipin.cn/playvinfo'
    c_key = get_ckey(vid, guid)
    params = {
        "callback": "jsonp1",
        "guid": guid,
        "platform": "4330701",
        "vid": vid,
        "defn": "auto",
        "charge": "0",
        "defaultfmt": "auto",
        "otype": "json",
        "defnpayver": "1",
        "appVer": "1.2.10",
        "sphttps": "1",
        "sphls": "1",
        "spwm": "4",
        "dtype": "3",
        "defsrc": "1",
        "encryptVer": "8.1",
        "sdtfrom": "4330701",
        "cKey": c_key,
        "panoramic": "false",
        "flowid": pid
    }
    res = requests.get(v_url, params=params, headers=headers, cookies={'guid': guid})
    json_data = res.text.strip('jsonp1(')[:-1]
    json_data = json.loads(json_data)
    data = json_data['vl']['vi'][0]
    url = data['ul']['ui'][0]['url']
    keyid = data['cl']['keyid']
    fvkey = data['fvkey']
    return f'{url}{keyid}?sdtfrom=4330701&guid={guid}*vkey={fvkey}&platform=2'


def main():
    try:
        video_url = 'https://w.yangshipin.cn/video?type=0&vid=p000016yi72'
        vid = video_url.split('vid=')[1]
        guid, pid = get_guid_pid()
        vurl = get_vurl(vid, guid, pid)
        up_url = 'https://btrace.yangshipin.cn/kvcollect?BossId=2865'
        params = {
            "ctime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            "ua": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/104.0.0.0 safari/537.36",
            "hh_ua": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/104.0.0.0 safari/537.36",
            "platform": "4330701",
            "guid": guid,
            "Pwd": "1698957057",
            "version": "wc-1.2.10",
            "url": video_url,
            "hh_ref": video_url,
            "vid": vid,
            "isfocustab": "1",
            "isvisible": "1",
            "idx": "0",
            "val": "365",
            "pid": pid,
            "bi": "0",
            "bt": "0",
            "defn": "hd",
            "vurl": vurl,
            "step": "6",
            "val1": "1",
            "val2": "1",
            "fact1": "",
            "fact2": "",
            "fact3": "",
            "fact4": "",
            "fact5": ""
        }
        requests.post(up_url, params=params, headers=headers)
        print('success')
    except Exception as e:
        print('errors', e)


if __name__ == '__main__':
    start_time = time.time()
    headers = {
        'referer': 'https://w.yangshipin.cn/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    with ThreadPoolExecutor(32) as f:
        for i in range(3000):
            f.submit(main)
    print(time.time() - start_time)
    print('over')
