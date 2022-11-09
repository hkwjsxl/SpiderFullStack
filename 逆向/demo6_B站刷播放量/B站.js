// e是时间戳
o = function (e) {
    // t
    return Math.ceil(e).toString(16).toUpperCase()  // 将时间戳变成十六进制再转大写
}


// e=8
a = function (e) {
    for (var t = "", n = 0; n < e; n++)
        t += o(16 * Math.random());  // 8位十六进制的大写字符串
    return s(t, e)
}
// 将一个0~16的数字转为十六进制再转大写
o = function (e) {
    return Math.ceil(e).toString(16).toUpperCase()
}
s = function (e, t) {
    var n = "";
    if (e.length < t)  // 小于8位前面补零
        for (var r = 0; r < t - e.length; r++)
            n += "0";
    return n + e
}
