from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.set_page_load_timeout(10)

browser.get('https://nairaland.com')
browser.maximize_window()
browser.implicitly_wait(5)

browser.find_element_by_xpath("/html/body/div/table[1]/tbody/tr/td/b[2]/a").click()
browser.find_element_by_name("name").send_keys('Mrquote')
browser.find_element_by_name("password").send_keys('arinze1020')
browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[2]/td/form/input[3]").click()
time.sleep(5)
browser.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[2]/td/a[3]").click()
time.sleep(5)
browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[2]/td/p[1]/a[1]").click()
time.sleep(5)
browser.find_element_by_name("body").send_keys('Reader you hahahahah')
browser.find_element_by_xpath("/html/body/div/table[2]/tbody/tr/td/form/p[2]/input[1]").click()

time.sleep(5)
browser.quit