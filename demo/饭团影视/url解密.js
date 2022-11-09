var CryptoJS = require("crypto-js")

var t = CryptoJS["AES"]["decrypt"]("pmDOfzWbg/o3JtiWq6T0q5g530Huvl5OyWvOlXwkcr2t3GhzLAhuU1Mj5b8Bfzea5l0LjlT6IvgyOH36JqIE7gAVDh2+5Vq7KA2HBYsCRPRvvAZg9O0JaO1c8BH5w2iqih/WHFpogZXn+ndakMqHErfWY6jm7zjKs3COy/xmhPWbZ+wOLINPcB10BNlzf4Do",
    CryptoJS["enc"]["Latin1"]['parse']("Of84ff0clf252cba"), {
        'iv': CryptoJS["enc"]["Latin1"]["parse"]("c487ebl2e38a0faO"),
        'mode': CryptoJS["mode"]['CBC'],
        'adding': CryptoJS['pad']["ZeroPadding"]
    })['toString'](CryptoJS["enc"]['Utf8'])

console.log(t)

