from selenium import webdriver
from selenium.webdriver import ActionChains
import time


# 创建编辑器
driver = webdriver.Chrome()

# 打开页面
driver.get(r"http://www.baidu.com/")

# 窗口最大化
driver.maximize_window()

# 输入框
ele = driver.find_element_by_xpath("//*[@id='kw']")

# 创建actionchains
ac = ActionChains(driver)

# 点击输入框
ele.click()

# 模拟键盘录入a
ac.key_down("a").key_up("a").perform()

time.sleep(3)

# 关闭页面
driver.quit()