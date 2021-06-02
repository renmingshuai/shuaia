from  selenium import  webdriver
import time
webdriver=webdriver.Chrome()
webdriver.maximize_window()
webdriver.get(r"https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0c537319b26d46ea908e84ec6cf07e92")
webdriver.find_element_by_xpath("//*[@id='ttbar-login']/a[1]").click()
webdriver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
webdriver.find_element_by_xpath("//*[@id='loginname']").send_keys("13008016530")
webdriver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("s1075576058")
webdriver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(8)

webdriver.find_element_by_xpath("//*[@id='key']").send_keys("电脑")
webdriver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(3)
webdriver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()
#加载所有的标签
all=webdriver.window_handles
print(all)
#切换标签
webdriver.switch_to.window(all[1])
webdriver.find_element_by_link_text("【新】8核i7 RTX2060 240Hz").click()
time.sleep(3)
webdriver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(3)
webdriver.quit()