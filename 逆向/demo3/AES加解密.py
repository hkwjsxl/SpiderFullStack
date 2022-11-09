from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 加密
word = '春风十里不如你，jay'
key = b'0123456789012345'
iv = b'1234567890123456'
aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
word = pad(word.encode('utf-8'), 16)
dec_bytes = aes.encrypt(word)
print(dec_bytes)
b64_str = base64.b64encode(dec_bytes).decode()
print(b64_str)
print('-------------------')

# 解密
b64_bytes = base64.b64decode(b64_str)
key = b'0123456789012345'
iv = b'1234567890123456'
aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
word = aes.decrypt(b64_bytes)
print(word)
word_unpad = unpad(word, 16)
print(word_unpad)
src_word = word_unpad.decode('utf-8')
print(src_word)





