from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
list = browser.find_elements_by_css_selector('.service-bd li')  # 获取多个节点，返回类型是列表
print(list,sep='\n')
list2 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(list2)
browser.close()