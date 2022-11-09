
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
        document.cookie=('_')+('_')+('j')+('s')+('l')+('_')+('c')+('l')+('e')+('a')+('r')+('a')+('n')+('c')+('e')+('=')+(-~false+'')+(-~[5]+'')+(3+3+'')+(-~[2]+'')+((1<<2)+'')+(9+'')+(~~[]+'')+(1+3+'')+((1+[2]>>2)+'')+(3+4+'')+('.')+(1+[0]-(1)+'')+(-~false+'')+(-~0+'')+('|')+('-')+(-~false+'')+('|')+('s')+(2+3+'')+(1+8+'')+((1+[2]>>2)+'')+('J')+('a')+('P')+(1+6+'')+('U')+('L')+('L')+('j')+('Z')+('O')+('J')+('H')+('s')+((1+[4]>>1)+'')+('Q')+('W')+('t')+('C')+('j')+('Y')+([2]*(3)+'')+('B')+('c')+('%')+(3+'')+('D')+(';')+('m')+('a')+('x')+('-')+('a')+('g')+('e')+('=')+(-~[2]+'')+(6+'')+(~~false+'')+((+false)+'')+(';')+('p')+('a')+('t')+('h')+('=')+('/');location.href=location.pathname+location.search;
                var fn = function () {
                    return document.cookie
                }
            