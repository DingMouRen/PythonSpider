from urllib.parse import unquote
'''
unquote()函数可以进行URL解码
http://www.baidu.com?name=小明
'''
url = 'http://www.baidu.com?name=%E5%B0%8F%E6%98%8E'
print(unquote(url))