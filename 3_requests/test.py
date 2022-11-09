import os.path

print(2 or 3)
print(2 and 0 and 3)
a = ['1', '2']
b = [3, 4]
c = [5, 6]
d = (1, 2)
e = (3, 4)
print(sum((a, b, c), []))
print(sum((d, e), ()))
a = 257
b = 257
print(a is b)
print(id(a))
print(id(b))

s1 = "hell o"
s2 = "hell o"
print(s1 is s2)

from distutils.sysconfig import get_python_lib

print(get_python_lib())


# import this
# import antigravity

def func():
    try:
        return 'try'
    finally:
        # return 'finally'
        ...


print(func())
print('abc'.count(''))
print('' in 'a')
print('' < str(100))
print(c[100:])
a = 'hello'
print(id(a))
b = 'he' + 'llo'
print(id(b))

a, b = '1', '1'
print(a is b)
print('a' * 20 == 'aaaaaaaaaaaaaaaaaaaa')

s = 'abc'
print(s.find('d'))  # -1

print(os.getcwd())
