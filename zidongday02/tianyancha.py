from  selenium import  webdriver
import  time
from  selenium.webdriver import  ActionChains
webdriver=webdriver.Chrome()
webdriver.get("https://www.qcc.com")
webdriver.maximize_window()
time.sleep(3)
webdriver.find_element_by_xpath("//*[@id='addfavorModal']/div/div/div[1]/img[1]").click()
webdriver.find_element_by_link_text("登录 | 注册").click()
time.sleep(6)
huadong=webdriver.find_element_by_xpath("//*[@id='nc_1_n1z']")
#创建Actionchain
ac=ActionChains(webdriver)
#click_and_hold模拟按住鼠标左键在源元素上，点击并且不释放         release()松开鼠标按键
ac.click_and_hold(huadong).move_by_offset(348,0).perform()
time.sleep(6)
webdriver.quit()