from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


# 生成key
# key = RSA.generate(1024)
# # 私钥
# pri_key = key.export_key()
# print(pri_key)
# with open('pri_key.pem', 'wb') as f:
#     f.write(pri_key)
# # 公钥
# pub_key = key.public_key().export_key()
# print(pub_key)
# with open('pub_key.pem', 'wb') as f:
#     f.write(pub_key)

with open('pri_key.pem', 'rb') as f:
    pri_key = f.read()
with open('pub_key.pem', 'rb') as f:
    pub_key = f.read()

# print(pri_key)
# print(pub_key)

# word = '我爱你'
# pub_key = RSA.import_key(pub_key)
# rsa = PKCS1_v1_5.new(key=pub_key)
# print(rsa.encrypt(word.encode('utf-8')))

enc_bytes = b"\x9e_\x9et\t\xa1\x02\xe6\x0eM\x8e*\xcf\x88\xe2B\xf2h>[\xdbC\xb9\x14\xc9\x19*CD\xf7\xd7\xc9I\xeaQ\xe8\x89D^C\x85)j]\x07\\\xa4l\x90:\xbaX\xcf6d\x14{\xb4\xcbU\x8eZ\x19,6\x19\xf0\xf5k\xcc\xf4^\xb4\x84O\xe4Q\x86Ou\x10\xa8\x16\x17\xf3\xb1\x02\x96u\x1cR\x01\xd1!\x860!\xf9\x03\xd95\x8fP\x1e\xa0\xafF\xd8\xc3W\xa8\xc3s|\xe9'\xaa\xda.V\xf3\r\x1f\xbc(\xac`\x04"

pri_key = RSA.import_key(pri_key)
rsa = PKCS1_v1_5.new(key=pri_key)
data = rsa.decrypt(enc_bytes, None)
print(data.decode('utf-8'))





