from urllib import request,error
import socket

'''
HTTPError是URLError的子类，专门处理HTTP请求错误的，比如认证请求失败等，有3个属性
code:返回HTTP的状态码，比如404表示网页不存在，500表示服务器内部的错误
reson:同父类URLError一样，返回错误的原因，有的时候返回字符串，有的时候会返回对象
headers:返回请求头

推荐的异常处理写法：1.先捕获子类的异常 2.再捕获父类的异常
'''

# 1.reason返回的是字符串类型
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n') # sep='' 在三个参数之间添加字符串，这里添加的是换行符
except error.URLError as e:
    print(e.reason)
else:
    print("请求成功")

# 2.reason返回的是对象
try:
    response2 = request.urlopen('http://www.baidu.com',timeout=0.001)
except error.HTTPError as e:
    print('捕获到HTTPError类型异常',e.reason,e.code,e.headers,sep='\n')
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("HTTPError的reason返回的是对象，TIME OUT")
except error.URLError as e:
    print('捕获到URLError类型异常',e.reason,sep='\n')
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("URLError的reason返回的是对象，TIME OUT")
else:
    print("请求成功")