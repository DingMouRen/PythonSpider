'''
urlopen()函数
'''

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8')) # 输出网页的html的源代码
print(type(response)) # 输出响应的类型，<class 'http.client.HTTPResponse'> 是HTTPResponse类型的对象