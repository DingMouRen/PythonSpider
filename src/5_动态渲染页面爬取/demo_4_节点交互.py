from selenium import webdriver
import time
'''
Chrome与chromedriver版本必须对应，否则无法交互

'''
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_search = browser.find_element_by_id('q')
input_search.send_keys('iphone')
time.sleep(1)
input_search.clear()
input_search.send_keys('荣耀play')
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()