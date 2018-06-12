from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_elements_by_id('q') # 通过id获取输入框节点
input_second = browser.find_elements_by_css_selector('#q') # 通过css选择器获取输入框节点
input_third = browser.find_elements_by_xpath('//*[@id="q"]') #通过xpath获取输入框节点
print(input_first,input_second,input_third,sep='\n')
browser.close()