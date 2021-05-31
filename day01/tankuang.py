from  selenium import  webdriver
import  time
cs=webdriver.Chrome()
cs.get(r"file:///C:/Users/baba123/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E4%BB%B6%E5%A4%B9%20(2)/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E5%BC%B9%E6%A1%86%E7%9A%84%E9%AA%8C%E8%AF%81/dialogs.html")
cs.maximize_window()
cs.find_element_by_id("alert").click()

time.sleep(3)
cs.switch_to.alert.accept()

cs.find_element_by_id("confirm").click()
time.sleep(9)
cs.switch_to.alert.dismiss()       #accept    确定           #dismiss取消
time.sleep(6)
cs.quit()
