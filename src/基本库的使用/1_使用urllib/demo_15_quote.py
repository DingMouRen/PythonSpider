from urllib.parse import quote

'''
quote()函数可将中文参数转变成URL编码，避免乱码问题
http://www.baidu.com?name=%E5%B0%8F%E6%98%8E
'''
keyword = '小明';
url = 'http://www.baidu.com?name='+quote(keyword)
print(url)