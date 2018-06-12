from selenium import webdriver

browser = webdriver.Chrome() # 声明浏览器对象
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()