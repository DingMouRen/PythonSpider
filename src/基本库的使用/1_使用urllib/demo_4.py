from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError
'''
验证：用户名和密码
'''
username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm
p.add_password(None,url,username,password) # 添加进去用户名和密码
auth_handler = HTTPBasicAuthHandler(p) # 构建一个处理验证的Handler
opener = build_opener(auth_handler) # opener比urlopen() Request更加深一层

try:
    result = opener.open(url) # opener发起请求时，说明验证已经成功了，获取的结果就是验证成功后页面源码内容
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
