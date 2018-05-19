import requests

'''
Session模拟同一个会话而不担心Cookie的问题。通常用于模拟登陆之后再进行下一步操作
'''

session_1 = requests.Session()
response_1 = session_1.get('http://httpbin.org/cookies/set/number/123456')
response_2 = session_1.get('http://httpbin.org/cookies')
print("response_1的cookies:",response_1.text)
print("response_2的cookies:",response_2.text)
