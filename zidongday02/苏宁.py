from  selenium import  webdriver
import time
webdriver=webdriver.Chrome()
webdriver.maximize_window()
webdriver.get("https://www.suning.com/?utm_source=baidu&utm_medium=brand&utm_campaign=title&utm_term=brand")
webdriver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")
webdriver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)
webdriver.find_element_by_xpath("//*[@id='pop418']/a").click()
webdriver.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_01:0000000000_12157019776']/i/img").click()
all=webdriver.window_handles
webdriver.switch_to.window(all[1])
webdriver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[2]/a/span").click()
webdriver.find_element_by_xpath("//*[@id='yanbao']/dd/ul/li[2]/a/span").click()
webdriver.find_element_by_xpath("//*[@id='addCart']").click()
time.sleep(6)
webdriver.quit()