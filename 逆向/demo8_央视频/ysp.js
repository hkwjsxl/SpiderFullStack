function PID() {
    return `${(new Date).getTime().toString(36)}_${Math.random().toString(36).replace(/^0./, "")}`
}

// l7el7biy_7m43uqg8o4m


function GUID() {
    var t = (new Date).getTime().toString(36)
    var r = Math.random().toString(36).replace(/^0./, "");
    return "".concat(t, "_").concat(r);
}

console.log(GUID())

// vurl: '{v1-vi-0}{fn}?sdtfrom=4330701&guid={guid}&vkey={fvkey}&platform=2'


// Ue(vid, '时间戳', "1.2.10", guid, 4330701)
// Wn:"|1950939434|{vid}|{时间戳}|mg3c3b04ba|1.2.10|{guid}|4330701|https://w.yangshipin.cn/|mozilla/5.0 (windows nt ||Mozilla|Netscape|Win32|"
// Wn = Dt + qn + Gn
//    "|"  1950939434  "|p000016yi72|1661773893|mg3c3b04ba|1.2.10|l7ep2uj4_jgrq5zu0ihm|4330701|https://w.yangshipin.cn/|mozilla/5.0 (windows nt ||Mozilla|Netscape|Win32|"
// "4E2918885FD98109869D14E0231A0BF4"
// "16B17E519DDD0CE5B79D7A63A4DD801C"

// return "--01" + Wn
function f(Vn) {
    for (Mr = 0; Mr < Vn.length; Mr++)
    Xn = Vn["charCodeAt"](Mr),
        Yn = (Yn << -5516 + 1360 + 9081 - 4920) - Yn + Xn,
        Yn &= Yn;
    return Yn
}



