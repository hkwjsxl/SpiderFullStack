get_token = function () {
    for (var t = Math.round((new Date).getTime() / 1000).toString(), e = arguments.length, r = new Array(e), n = 0; n < e; n++)
        r[n] = arguments[n];
    r.push(t);
    var o = SHA1(r.join(",")).toString(i.enc.Hex)
        , s = i.enc.Base64.stringify(i.enc.Utf8.parse([o, t].join(",")));
    return s
}


console.log(get_token("/api/movie"))
