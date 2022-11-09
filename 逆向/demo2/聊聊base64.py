import base64

url = 'https://img0.baidu.com/it/u=4128086631,2090775151&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500'
url_byte = url.encode('utf-8')

b64_str = base64.b64encode(url_byte).decode()
print(b64_str)

_str = base64.b64decode(b64_str).decode()
print(_str)

# b64encode 字节---b64字符串
# b64decode b64字符串---字节

