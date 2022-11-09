import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 等待节点加载完成
driver.get("https://www.douban.com/search?q=%E6%9D%B0%E6%A3%AE%E6%96%AF%E5%9D%A6%E6%A3%AE")
time.sleep(2)
# 使用id的方式获取右上角的搜索框
# ret1 = driver.find_element(By.ID, 'inp-query')
# ret1 = driver.find_element(By.ID, 'inp-query').send_keys("杰森斯坦森")
# ret1 = driver.find_element_by_id("inp-query")
# print(ret1)

# 输出为：<selenium.webdriver.remote.webelement.WebElement (session="ea6f94544ac3a56585b2638d352e97f3", element="0.5335773935305805-1")>

# 搜索输入框  使用find_elements进行获取
# ret2 = driver.find_elements(By.ID, "inp-query")
# ret2 = driver.find_elements_by_id("inp-query")
# print(ret2)
#输出为：[<selenium.webdriver.remote.webelement.WebElement (session="ea6f94544ac3a56585b2638d352e97f3", element="0.5335773935305805-1")>]

# 搜索按钮  使用xpath进行获取
# ret3 = driver.find_elements(By.XPATH, '//*[@id="inp-query"]')
# ret3 = driver.find_elements_by_xpath("//*[@id="inp-query"]")
# print(len(ret3))
# print(ret3)

# 匹配图片标签
ret4 = driver.find_elements(By.TAG_NAME, 'img')
for url in ret4:
    print(url.get_attribute('src'))

# ret4 = driver.find_elements_by_tag_name("img")
print(len(ret4))

ret5 = driver.find_elements(By.LINK_TEXT, "浏览发现")
# ret5 = driver.find_elements_by_link_text("浏览发现")
print(len(ret5))
print(ret5)

ret6 = driver.find_elements(By.PARTIAL_LINK_TEXT, "浏览发现")
# ret6 = driver.find_elements_by_partial_link_text("浏览发现")
print(len(ret6))
# 使用class名称查找
ret7 = driver.find_elements(By.CLASS_NAME, 'nbg')
print(ret7)
# driver.close()

