import urllib.parse
import urllib.request
import urllib.error
import socket

'''
为链接传递一些参数
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None):

* data参数：1.需要通过bytes()函数将内容转化为字节流 2.请求方式为post
* timeout参数: 如果请求超出了设置的超时时间，还没有响应，就会抛出异常.我们可以通过try except来跳过它的抓取
'''

# 1.传递data参数
data = bytes(urllib.parse.urlencode({'name':'小明'}),encoding='utf-8')
response1 = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response1.read().decode('utf-8'))

# 2.设置超时时间
try:
    response2 = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    print(response2.read().decode('utf-8'))
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('请求超时')