'''
urlopen()函数

HTTPResponse实例包装来自服务器的HTTP响应
'''

import urllib.request

response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8')) # 输出网页的html的源代码
print('类型:',type(response)) # 输出响应的类型，<class 'http.client.HTTPResponse'> 是HTTPResponse类型的对象
print('headers:',response.getheaders()) # 输出响应的header的元组列表
print('fileno:',response.fileno())    # 输出响应底层套接字的fileno
print('msg:',response.msg)
print('http协议版本:',response.version)
print('响应状态码:',response.status)
print('响应的原因短语:',response.reason)



