from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print('id:',input.id)
print('location:',input.location)
print('tag_name',input.tag_name)
print('size:',input.size)
print('text:',input.text)
browser.close()