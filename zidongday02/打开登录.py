from  selenium import webdriver
import time
webdriver=webdriver.Chrome()
webdriver.get(r"file:///C:/Users/baba123/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(2)/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E8%B7%B3%E8%BD%AC%E9%A1%B5%E9%9D%A2/pop.html")
webdriver.maximize_window()
webdriver.find_element_by_xpath("//*[@id='goo']").click()
#获取所以窗口
all=webdriver.window_handles

#切换操作
webdriver.switch_to.window(all[1])
webdriver.find_element_by_xpath("//*[@id='kw']").send_keys("我是你爸爸")
webdriver.find_element_by_xpath("//*[@id='su']").click()
time.sleep(6)
webdriver.quit()