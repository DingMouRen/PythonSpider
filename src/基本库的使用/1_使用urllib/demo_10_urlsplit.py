from urllib.parse import urlsplit,urlunsplit

'''
urlsplit()函数类似于urlparse()函数，不同的是只返回5个结果，将params合并到path中，
SplitResult是一个元组

与之对应的函数urlunsplit()将长度为5的可迭代对象，构建成URL
'''
splitResult = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(type(splitResult),splitResult,sep='\n')

data = ['http','www.baidu.com','index.html','id=6','comment']
url = urlunsplit(data)
print(url)