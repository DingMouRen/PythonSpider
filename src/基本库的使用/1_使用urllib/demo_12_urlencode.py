from urllib.parse import urlencode
'''
urlencode()函数可以将字典形式的参数序列化成GET请求的参数
'''
params = {
    'id':'666',
    'name':'jack'
}
base_url = 'http://www.baidu.com?'
result_url = base_url + urlencode(params)
print(result_url)