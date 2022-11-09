function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(data, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(data)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}

function c(a, b, c) {
    // var d, e;
    // setMaxDigits(131);
    // d = new RSAKeyPair(b,"",c);
    // e = encryptedString(d, a);
    // return e
    return '7421d3ee3b3121e77af356e340685399705e6f1a47e62217cc074da675dabe566dda1df3c5116a4d7cde5390dc9490fdecc9f30959fb47a43016fdee6e54f79b12f283cf5c2478712c01232352bea5ac388d3155e4fc1570f819a3a9b57aa2720c6cb09f48a95c3c71b14055686d54da5c19b5880f068d829b527540715e658b'
}

function d(d, e, f, g) {
    var h = {}
    // var i = a(16);
    var i = 'Chcmd7MmUWBL3J72'
    h.encText = b(d, g);  // 对数据aes加密，iv="0102030405060708",密钥是g，mode_CBC

    h.encText = b(h.encText, i);  // 对数据再次加密，iv="0102030405060708",密钥是i

    h.encSecKey = c(i, e, f);  //
    return h
}
