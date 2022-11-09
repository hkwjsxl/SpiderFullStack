byte_list = [-26, -83, -90, -26, -78, -101, -23, -67, -112]

bs = bytearray()  # python字节数组
for item in byte_list:
    if item < 0:
        item = item + 256
    bs.append(item)

str_data = bs.decode('utf-8')  # data = bytes(bs)
print(str_data)

