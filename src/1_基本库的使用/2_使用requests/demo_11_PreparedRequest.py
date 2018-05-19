from requests import Request,Session
'''
将请求封装成一个对象，在进行队列调度时会非常方便，可以构造一个Request队列
1.用url data headers参数构造一个Request对象，
2.调用Session的prepare_request()方法将Request对象转换成一个PreparedRequest对象
3.调用send()函数，发送请求
'''
url = 'http://httpbin.org/post'
data = {
    'name':'Jacck'
}
headers = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
session_1 = Session()
request_1 = Request('POST',url,data=data,headers=headers)
preparedRequest_1 = session_1.prepare_request(request_1)
response_1 = session_1.send(preparedRequest_1)
print(response_1.text)