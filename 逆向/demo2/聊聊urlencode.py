from urllib.parse import quote, unquote

word = '周杰伦'


val = quote(word)
print(val)

val = unquote(val)
print(val)

