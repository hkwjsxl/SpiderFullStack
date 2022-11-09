from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


url = 'https://www.baidu.com/'
# 加启动配置
option = ChromeOptions()
# 启动开发者模式(关闭chrome控制)
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", 'False')
# 跳过滑块验证
option.add_argument('--disable-blink-features=AutomationControlled')
chrome = Chrome(options=option)
chrome.implicitly_wait(10)
chrome.get(url)
chrome.implicitly_wait(10)
chrome.maximize_window()
chrome.implicitly_wait(10)
# print(chrome.title)
# print(chrome.page_source)
#
chrome.find_element(By.XPATH, '//*[@id="kw"]').send_keys('Python')
chrome.find_element(By.XPATH, '//*[@id="su"]').click()
chrome.implicitly_wait(10)
print(chrome.get_cookies())
print(chrome.current_url)

# 1. 获取当前所有的窗口
current_windows = chrome.window_handles

# 2. 根据窗口索引进行切换
chrome.switch_to.window(current_windows[1])

chrome.switch_to.window(chrome.window_handles[-1])  # 跳转到最后一个窗口
chrome.switch_to.window(current_windows[0])  # 回到第一个窗口




