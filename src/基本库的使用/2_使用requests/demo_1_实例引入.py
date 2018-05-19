import requests
'''
requests.get()
requests.post()
requests.delete()
requests.head()
requests.put()
requests.options()
'''
response1 = requests.get('https://www.baidu.com')
print('返回对象类型：',type(response1))
print('响应状态码:',response1.status_code)
print('text类型:',type(response1.text))
print('响应的text',response1.text)
print('Cookie的类型:',type(response1.cookies))
print('响应的cookie信息:',response1.cookies)
