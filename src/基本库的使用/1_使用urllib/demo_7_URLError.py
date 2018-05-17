from urllib import request,error

'''
request模块产生的异常都可以用URLError来处理
URLError类来自error模块，继承自OSError,OSError是error模块的基类，
通过URLError处理错误，避免程序异常终止，同时将异常得到有效的处理
'''
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason) # reason返回错误的原因