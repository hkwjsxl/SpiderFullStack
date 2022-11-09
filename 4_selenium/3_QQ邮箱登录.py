from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


url = 'https://mail.qq.com/'
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

frame = chrome.find_element(By.ID, 'login_frame')
chrome.switch_to.frame(frame)
chrome.find_element(By.ID, 'switcher_plogin').click()

chrome.implicitly_wait(10)

chrome.find_element(By.ID, 'u').send_keys('562172420')
chrome.find_element(By.ID, 'p').send_keys('hH20020224.')
chrome.find_element(By.ID, 'login_button').click()





