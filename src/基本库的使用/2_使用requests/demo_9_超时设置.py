import requests

'''
超时时间是指发出请求到服务器返回响应的时间，
'''
response_1 = requests.get('https://www.taobao.com',timeout=1) # 超时时间设置为1秒，如果1秒后没有响应，就抛出异常
response_2 = requests.get('https://www.taobao.com',timeout=None) # 超时时间设置为永久等待，或者不写timeout也是可以的
