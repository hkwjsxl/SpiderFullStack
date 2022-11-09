from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs
from hashlib import md5, sha1, sha256


def first_req(url):
    res = session.get(url, headers=session.headers)
    __jsluid_h = session.cookies.get('__jsluid_h')
    if __jsluid_h:
        session.cookies.pop('__jsluid_h')
        session.cookies.update({
            '__jsluid_s': __jsluid_h
        })
    with open('first.js', 'w', encoding='utf-8') as f:
        f.write("""
            const jsdom = require("jsdom");
            const {JSDOM} = jsdom;
            
            const resourceLoader = new jsdom.ResourceLoader({
                userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
            });
            
            const html = `<!DOCTYPE html><p>Hello world</p>`;
            const dom = new JSDOM(html, {
                url: "https://www.cnvd.org.cn/webinfo/show/7541",
                referrer: "https://www.cnvd.org.cn/webinfo/show/7541",
                contentType: "text/html",
                resources: resourceLoader,
            });
            
            
            //window = {}
            window = global;
            
            const params = {
                location: {
                    hash: "",
                    host: "www.cnvd.org.cn",
                    hostname: "www.cnvd.org.cn",
                    href: "https://www.cnvd.org.cn/webinfo/show/7541",
                    origin: "https://www.cnvd.org.cn/webinfo/show/7541",
                    pathname: '/webinfo/show/7541',
                    port: "",
                    protocol: "https:",
                    search: "",
                },
                navigator: {
                    appCodeName: "Mozilla",
                    appName: "Netscape",
                    appVersion: "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
                    cookieEnabled: true,
                    deviceMemory: 8,
                    doNotTrack: null,
                    hardwareConcurrency: 4,
                    language: "zh-CN",
                    languages: ["zh-CN", "zh"],
                    maxTouchPoints: 0,
                    onLine: true,
                    platform: "MacIntel",
                    product: "Gecko",
                    productSub: "20030107",
                    userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
                    vendor: "Google Inc.",
                    vendorSub: "",
                    webdriver: false
                }
            };
            
            Object.assign(global, params);
            document = dom.window.document;
        """)
    with open('first.js', 'a', encoding='utf-8') as f:
        f.write(res.text.strip('<script>').strip('</script>') + ';')
        f.write("""
                var fn = function () {
                    return document.cookie
                }
            """)
    with open('first.js', 'r', encoding='utf-8') as f:
        js = execjs.compile(f.read())
    __jsl_clearance_s = js.call('fn')
    __jsl_clearance_s = __jsl_clearance_s.split('=')[1]
    print(__jsl_clearance_s)
    session.cookies.update({
        '__jsl_clearance_s': __jsl_clearance_s
    })


def second_req(url):
    session.headers.update({
        'Referer': 'https://www.cnvd.org.cn/webinfo/show/7541'
    })
    res = session.get(url, headers=session.headers, cookies=session.cookies)
    print(session.cookies)
    print(res.text)


def get_auth(params_dic):
    hash_type = params_dic['ha']
    i = j = 0
    while i < len(params_dic['chars']):
        while j < len(params_dic['chars']):
            a = params_dic['bts'][0] + params_dic['chars'][i:i + 1] + \
                params_dic['chars'][j:j + 1] + params_dic['bts'][1]
            if enc_hash(hash_type, a) == params_dic['ct']:
                return [params_dic['ct'], 3]


def enc_hash(enc_type, param):
    if enc_type == 'md5':
        enc_obj = md5()
    if enc_type == 'sha1':
        enc_obj = sha1()
    if enc_type == 'sha256':
        enc_obj = sha256()
    enc_obj.update(param.encode('utf-8'))
    return enc_obj.hexdigest()


def set_cookies(params, params_dic):
    __jsl_clearance_s = params[0] + ';Max-age=' + params_dic['vt'] + '; path = /'
    print(__jsl_clearance_s)
    session.cookies.update({
        '__jsl_clearance_s': __jsl_clearance_s
    })


def main():
    url = 'http://www.cnvd.org.cn/webinfo/show/7541'
    first_req(url)
    second_req(url)
    # params_dic = {
    #     "bts": ["1663470408.767|0|IcG", "imnOhTuOKVZ%2Fvcf3vlzV84%3D"],
    #     "chars": "cspLCMknXzfItQizLfpSEk",
    #     "ct": "c7a3b14e42067e7905774002884c5100",
    #     "ha": "md5",
    #     "tn": "__jsl_clearance_s",
    #     "vt": "3600",
    #     "wt": "1500"
    # }
    # params = get_auth(params_dic)
    # print(params)
    # set_cookies(params, params_dic)


if __name__ == '__main__':
    session = requests.session()
    session.headers.update({
        "Host": "www.cnvd.org.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    main()
