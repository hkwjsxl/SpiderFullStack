from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64


word = '春风十里不如你，jay'
key = b'01234567'
iv = b'12345678'
des = DES.new(key=key, iv=iv, mode=DES.MODE_CBC)
word = pad(word.encode('utf-8'), 8)
dec_bytes = des.decrypt(word)
print(dec_bytes)
base_str = base64.b64encode(dec_bytes).decode()
print(base_str)
print('-------------------------------')

key = b'01234567'
iv = b'12345678'
des = DES.new(key=key, iv=iv, mode=DES.MODE_CBC)
base_bytes = base64.b64decode(base_str)
print(base_bytes)
enc_bytes = des.encrypt(base_bytes)
print(enc_bytes)
enc_unpad = unpad(enc_bytes, 8)
print(enc_unpad)
word = enc_unpad.decode('utf-8')
print(word)



