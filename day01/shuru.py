from  selenium import  webdriver
import  time
driver=webdriver.Chrome()
driver.get(r"file:///C:/Users/baba123/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(2)/%E7%BB%83%E4%B9%A0%E7%9A%84html/frame.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='input1']").send_keys("我是你爸爸")
time.sleep(3)
driver.quit()