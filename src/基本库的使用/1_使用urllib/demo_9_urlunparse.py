from urllib.parse import urlunparse

'''
urlunparse()函数接受一个长度为6的可迭代对象(长度必须是6)，构造URL
http://www.baidu.com/index.html;user?id=6#comment
'''
data = ['http','www.baidu.com','index.html','user','id=6','comment']
url = urlunparse(data)
print(type(url),url,sep='\n')