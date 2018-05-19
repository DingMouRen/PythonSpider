import requests

'''
上传文件 
'''

filesUp = {
    'file': open('favicon.ico','rb')
}
response = requests.post('http://httpbin.org/post',files=filesUp)
print(response.text)