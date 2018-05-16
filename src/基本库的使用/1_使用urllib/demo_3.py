from urllib import request,parse
import urllib.request

'''
Request构造函数
class urllib.request.Request( url, data=None, headers={}, origin_req_host=None, unverifiable=False,method=None):
url:必传参数
data:需要传递字节流类型数据，如果是字典的话，使用bytes(urllib.parse.urlencode({'name':'小明'}),encoding='utf-8')
headers:请求头，是字典类型，也可以通过Request实例通过函数add_header()添加
origin_req_host:是请求方的的host名称或ip地址
unverifiable:表示这个请求是否是无法验证的，默认是false,
method:指定请求的方法
'''

# 1.Request的基本使用
request1 = urllib.request.Request('http://python.org')
respose1 = urllib.request.urlopen(request1)
print("Request的基本使用")
print(respose1.read().decode('utf-8'))

# 2.传入多个参数构建请求
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'小明'
}
data = bytes(urllib.parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
respose2 = request.urlopen(req)
print("传入多个参数构建请求")
print(respose2.read().decode('utf-8'))