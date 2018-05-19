import requests

'''
指定一个本地证书当作客户端证书，可以是单个文件（包含密钥和证书）或者一个包含两个文件路径的元组
下面是演示代码，本地的私有证书的key必须是解密状态的
'''
response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
