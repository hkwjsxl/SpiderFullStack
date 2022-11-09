var enc_md5 = function () {
    return new o_init([1732584193, 4023233417, 2562383102, 271733878])
}

function o_init(e, n) {
    e = this.words = e || [],
        this.sigBytes = 4 * e.length
}

var _doFinalize = function (data) {
    var t = data
        , n = t.words
        , r = 8 * this._nDataBytes
        , o = 8 * t.sigBytes;
    n[o >>> 5] |= 128 << 24 - o % 32;
    var i = parseInt(parseFloat(r / 4294967296))
        , u = r;
    n[15 + (o + 64 >>> 9 << 4)] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
        n[14 + (o + 64 >>> 9 << 4)] = 16711935 & (u << 8 | u >>> 24) | 4278255360 & (u << 24 | u >>> 8),
        t.sigBytes = 4 * (n.length + 1),
        _process(data);
    for (var a = this._hash, c = t.words, l = 0; l < 4; l++) {
        var s = c[l];
        c[l] = 16711935 & (s << 8 | s >>> 24) | 4278255360 & (s << 24 | s >>> 8)
    }
    return a
}
var _process = function (t) {
    var n = t
        , r = n.words
        , o = n.sigBytes
        , i = this.blockSize
        , a = o / (4 * i)
        , c = 0
        , l = Math.min(4 * c, o);
    if (c) {
        for (var s = 0; s < c; s += i)
            this._doProcessBlock(r, s);
        var f = r.splice(0, c);
        n.sigBytes -= l
    }
    return new u_init(f, l)
}
var u_init = function (e, n) {
    e = this.words = e || [],
        this.sigBytes = n
}

var md5_result = enc_md5()
console.log(md5_result)
console.log(_doFinalize(md5_result))

var b64_stringify = function (e) {
    var t = e.words
        , n = e.sigBytes
        , r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    for (var o = [], i = 0; i < n; i += 3)
        for (var u = (t[i >>> 2] >>> 24 - i % 4 * 8 & 255) << 16 | (t[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255) << 8 | t[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, a = 0; a < 4 && i + .75 * a < n; a++)
            o.push(r.charAt(u >>> 6 * (3 - a) & 63));
    var c = r.charAt(64);
    if (c)
        for (; o.length % 4;)
            o.push(c);
    return o.join("")
}
var second_data = {
    'sigBytes': 16,
    'words': [1493458501, 1347097707, -878253122, 831674453]
}


var b64_resutl = b64_stringify(second_data)
console.log(b64_resutl)


function fn(t, n) {
    // "dfkcY1c3sfuw0Cii9DWjOUO3iQy2hqlDxyvDXd1oVMxwYAJSgeB6phO8eW1dfuwX"
    // "GET
    // https://gdtv-api.gdtv.cn/api/innerAd/v1/channelOperationAd
    // 1663823955958
    // "
    return new enc_HMAC(e, n).finalize(t)
}


function enc_HMAC(e, t) {
    e = this._hasher = new e.init,
    "string" == typeof t && (t = u.parse(t));
    var n = e.blockSize
        , r = 4 * n;
    t.sigBytes > r && (t = e.finalize(t));
    for (var o = this._oKey = t.clone(), i = this._iKey = t.clone(), a = o.words, c = i.words, l = 0; l < n; l++)
        a[l] ^= 1549556828,
            c[l] ^= 909522486;
    o.sigBytes = i.sigBytes = r;
}





