def fn():
    try:
        print('aaa')
        return '11'
    except:
        print('bbb')

    finally:
        print('ccc')
        return '22'


print(fn())
