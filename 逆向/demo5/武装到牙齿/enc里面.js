const asko6TByVl4b = "apA9P6kNUZLuIwM7";
const asijY4DsHyw4 = "b90IxF3cgyycpFOy";
const ackWfngxMOF7 = "dvRzX3seCLD4hBKS";
const acig0PHVUuRV = "fC36Uiz8Qb3srTTg";
const dskPvOvgJPgp = "h0KN50yK9Hy0t9Hc";
const dsiORr3rBjjI = "xEeegZWlHluJ0jXl";
const dckoeD81RzaW = "oUwr1ocHBMSKSZee";
const dcihmByg9JUA = "pVsmyTiDtMytu7AM";
const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

var BASE64 = {
    encrypt: function (text) {
        var b = new Base64();
        return b.encode(text)
    }, decrypt: function (text) {
        var b = new Base64();
        return b.decode(text)
    }
};
var DES = {
    encrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString()
    }, decrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString(CryptoJS.enc.Utf8)
    }
};
var AES = {
    encrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString()
    }, decrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString(CryptoJS.enc.Utf8)
    }
};
var localStorageUtil = {
    save: function (name, value) {
        var text = JSON.stringify(value);
        text = BASE64.encrypt(text);
        text = AES.encrypt(text, aes_local_key, aes_local_iv);
        try {
            localStorage.setItem(name, text)
        } catch (oException) {
            if (oException.name === 'QuotaExceededError') {
                localStorage.clear();
                localStorage.setItem(name, text)
            }
        }
    }, check: function (name) {
        return localStorage.getItem(name)
    }, getValue: function (name) {
        var text = localStorage.getItem(name);
        var result = null;
        if (text) {
            text = AES.decrypt(text, aes_local_key, aes_local_iv);
            text = BASE64.decrypt(text);
            result = JSON.parse(text)
        }
        return result
    }, remove: function (name) {
        localStorage.removeItem(name)
    }
};

function d7McpalOXek(pRIs8ok) {
    pRIs8ok = DES.decrypt(pRIs8ok, dskPvOvgJPgp, dsiORr3rBjjI);
    return pRIs8ok
}

function dHNzm0VKe1(pRIs8ok) {
    pRIs8ok = BASE64.decrypt(pRIs8ok);
    return pRIs8ok
}

function gKWRIWQLgcdJ8AAx(key, period) {
    if (typeof period === 'undefined') {
        period = 0
    }
    var d = DES.encrypt(key);
    d = BASE64.encrypt(key);
    var data = localStorageUtil.getValue(key);
    if (data) {
        const time = data.time;
        const current = new Date().getTime();
        if (new Date().getHours() >= 0 && new Date().getHours() < 5 && period > 1) {
            period = 1
        }
        if (current - (period * 60 * 60 * 1000) > time) {
            data = null
        }
        if (new Date().getHours() >= 5 && new Date(time).getDate() !== new Date().getDate() && period === 24) {
            data = null
        }
    }
    return data
}

function ObjectSort(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function (key) {
        newObject[key] = obj[key]
    });
    return newObject
}

function dZs9w70uMix(data) {
    data = AES.decrypt(data, asko6TByVl4b, asijY4DsHyw4);
    data = DES.decrypt(data, dskPvOvgJPgp, dsiORr3rBjjI);
    data = BASE64.decrypt(data);
    return data
}

var pILR8dI1cBW = (function () {
    function ObjectSort(obj) {
        var newObject = {};
        Object.keys(obj).sort().map(function (key) {
            newObject[key] = obj[key]
        });
        return newObject
    }

    return function (method, obj) {
        var appId = '3b67630882bc804fcba0de07c643667c';
        var clienttype = 'WEB';
        var timestamp = new Date().getTime();
        var param = {
            appId: appId,
            method: method,
            timestamp: timestamp,
            clienttype: clienttype,
            object: obj,
            secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
        };
        param = BASE64.encrypt(JSON.stringify(param));
        return param
    }
})();

function s3m068VrCwY577o3(mGtq5Y6xD, ooXovuFhRm, cG3mBJLR1, pMyrixA) {
    const k5Td = hex_md5(mGtq5Y6xD + JSON.stringify(ooXovuFhRm));
    const dLimJ = gKWRIWQLgcdJ8AAx(k5Td, pMyrixA);
    if (!dLimJ) {
        var pRIs8ok = pILR8dI1cBW(mGtq5Y6xD, ooXovuFhRm);
        $.ajax({
            url: '../apinew/aqistudyapi.php', data: {hXCrMSgFv: pRIs8ok}, type: "post", success: function (dLimJ) {
                dLimJ = dZs9w70uMix(dLimJ);
                onw5rR = JSON.parse(dLimJ);
                if (onw5rR.success) {
                    if (pMyrixA > 0) {
                        onw5rR.result.time = new Date().getTime();
                        localStorageUtil.save(k5Td, onw5rR.result)
                    }
                    cG3mBJLR1(onw5rR.result)
                } else {
                    console.log(onw5rR.errcode, onw5rR.errmsg)
                }
            }
        })
    } else {
        cG3mBJLR1(dLimJ)
    }
}