from selenium import webdriver
import time
webdriver=webdriver.Chrome()
webdriver.get(r"file:///C:/Users/baba123/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(2)/%E7%BB%83%E4%B9%A0%E7%9A%84html/main.html")
webdriver.maximize_window()
webdriver.switch_to.frame("frame")
webdriver.find_element_by_id("input1").send_keys("我是你爸爸")