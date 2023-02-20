## pip

~~~python
pip install pyqt5-tools -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
pip install --target=D:\Anaconda3\envs\py39\Lib\site-packages pygame -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
pip install --target=D:\Anaconda3\Lib\site-packages pygame -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

清华：https://pypi.tuna.tsinghua.edu.cn/simple/
阿里云:http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http ://pypi.hustunique. com/
山东理工大学：http: //pypi.sdutlinux. org/
中国科学技术大学：http://pypi.mirrors.ustc.edu.cn/simple/
豆瓣：http://pypi.douban.com/simple/
~~~

## 报错解决

~~~python
# 报错：UnicodeDecodeError: 'gbk' codec can't decode byte 0xd7 in position 5720: illegal multibyte sequence
# 解决：res.content.decode('gbk', errors='ignore')
~~~


##  自动下滑
~~~python
def drop_down():
    for x in range(1, 10, 2):
        time.sleep(0.5)
        j = x / 9
        # document.documentElement.scrollTop  # 指定滚动条的位置
        # document.documentElement.scrollTop  # 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
~~~

##  视频音频合并
~~~python
command = f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {title}output.mp4"
subprocess.run(command, shell=True)
# 或者
cmd = r'ffmpeg -i ' + 'data/' + title + '.mp4 -i ' + 'data/' + title + '.mp3 -acodec copy -vcodec copy ' + "data/" + title + 'out.mp4'
subprocess.run(cmd, shell=True)
~~~

## selenium

~~~python
from selenium.webdriver import Chrome, ChromeOptions
# 加启动配置
option = ChromeOptions()
# 配置无界面的谷歌浏览器
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')
# 启动开发者模式(关闭chrome控制)
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", 'False')
# 跳过普通滑块验证
# chrome的版本号小于88，在你启动浏览器的时候（此时没有加载任何网页内容），向页面嵌入js代码，去掉webdriver。
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",  {
    "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"""
    })
# chrome的版本大于等于88
option = Options()
option.add_experimental_option('excludeSwitches', ['enable-automation']
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)

"""selenium模板"""
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC # 等待操作需要导入的库
from selenium.webdriver.common.action_chains import ActionChains # 用于完成一系列操作
from selenium.webdriver.support.wait import WebDriverWait # 等待某个特定的操作
from selenium.webdriver.chrome.options import Options # 设置参数
from selenium.webdriver.support.select import Select # 专门用于处理下拉框
from selenium.webdriver.common.keys import Keys # 所有按键的指令
from selenium.webdriver.common.by import By # 指定搜索方法
import time
# 内核驱动参数
options = Options()
# 处理 SSL 证书错误问题、隐藏自动化操作、忽略无用的日志、禁用 GPU（默认添加）
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
options.add_argument('--disable-gpu')
# 无头浏览器，窗口调大，防止样式堆叠
options.add_argument("--headless")
options.add_argument("--window-size=4000,1600")
# 初始化
web = Chrome(options=options)
# 进入网站
web.get("http://www.baidu.com")
# 全局隐式等待 5 秒，即获取元素的函数超过 5 秒就报错超时
web.implicitly_wait(5)
"""
# 需要完成的操作
xxxxxxxxxxxxxxxx
"""
# 静待 10 秒，用于查阅页面
time.sleep(10)
# 关闭整个驱动
web.quit()

~~~

##  pd生成时间序列
~~~python
start = '20220101'
end = '20220303'
date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
print(date_list)
~~~

## 验证码识别
~~~python
# https://github.com/sml2h3/ddddocr
import ddddocr
ocr = ddddocr.DdddOcr()
with open("code.png", 'rb') as f:
    image = f.read()
code = ocr.classification(image)
print(code)
------
import pytesseract
result = pytesseract.image_to_string('img.png', lang='chi_sim')
~~~


## ob混淆一键还原
~~~python
# https://github.com/Tsaiboss/decodeObfuscator
node main.js Medium.js 666.js
# https://github.com/DingZaiHub/ob-decrypt
~~~


## 百度AI
~~~python
# https://ai.baidu.com/tech/ocr
from aip import AipOcr
APP_ID = '27751139'
API_KEY = 'kI9mTb6OhcW0ntr1TxEMdiRx'
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
with open('img.png', 'rb') as f:
    img_content = f.read()
result = client.basicGeneral(img_content)
res_list = []
for res in result['words_result']:
    res_list.extend(res['words'])
    print(res['words'])
print(len(res_list))
~~~



