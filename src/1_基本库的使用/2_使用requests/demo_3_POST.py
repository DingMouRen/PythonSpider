import requests

'''
POST请求
'''
data = {
    'name':'小红',
    'age':'18'
}

response = requests.post('http://httpbin.org/post',data=data)
print(response.text)