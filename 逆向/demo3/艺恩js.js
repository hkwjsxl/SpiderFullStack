// function success(e, t, n) {
//     1 == (e = "{" == e[0] ? JSON.parse(e) : JSON.parse(webInstace.shell(e)))
//         .Status || 200 == e.Code ? r(e.Data) : 200 == e.code ? r(e.data) : a(e.Msg)
// }


var webDES = function () {
                    // data, a, 1
    var func = function (a, b, c) {
        if (0 == b)
            // return a[c:]
            return a['substr'](c);
        var d;
        // d = '' + a[:b]
        d = '' + a['substr'](0, b);
        // return d += a[b+c:]
        return d += a['substr'](b + c);
    };

    this['shell'] = function (data) {

        if (!navigator || !navigator['userAgent'])
                        return '';

        if ((null == data) || (16 >= data['length']))
                        return data;
        // 取最后一个16进制字符转 十进制后 +9
        var a = parseInt(data[data['length'] - 1], 16) + 9
        // 取出第a个字符转为十进制
        var b = parseInt(data[a], 16);
        
        data = func(data, a, 1);
        // data[b:b+8]
        a = data['substr'](b, 8);

        data = func(data, b, 8);
        // utf-8
        b = _grsa_JS['enc']['Utf8']['parse'](a);

        a = _grsa_JS['enc']['Utf8']['parse'](a);
        // DES解码  ECB
        a = _grsa_JS['DES']['decrypt']({
                        'ciphertext': _grsa_JS['enc']['Hex']['parse'](data)  // 16进制
                    }, b, {
                        'iv': a,
                        'mode': _grsa_JS['mode']['ECB'],
                        'padding': _grsa_JS['pad']['Pkcs7']
                    })['toString'](_grsa_JS['enc']['Utf8'])
        ;
        return a['substring'](0, a['lastIndexOf']('}') + 1);
    }
    ;
}
    , webInstace = new webDES();
