from  selenium import  webdriver
import  time
driver=webdriver.Chrome()
driver.get(r"file:///C:/Users/baba123/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(2)/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E8%B7%B3%E8%BD%AC%E9%A1%B5%E9%9D%A2/pop.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='goo']").click()
driver.find_element_by_id("kw").send_key("撒大苏打撒")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()