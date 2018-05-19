import requests

'''
直接传一个元组进行验证,请求会自动验证成功，返回200状态码，验证失败返回401
提供了其他的验证方式，看书137页
'''
response = requests.get('http://local:5000',auth=('username','password'))