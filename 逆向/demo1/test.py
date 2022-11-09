from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


f = open('test.js', 'r', encoding='utf-8')
js = execjs.compile(f.read())
print(js.call('fn', 1, 2))


