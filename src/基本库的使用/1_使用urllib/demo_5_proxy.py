from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
'''
代理
运行会有错误：
UnicodeError: encoding with 'idna' codec failed (UnicodeError: label empty or too long)
'''

proxy_handler = ProxyHandler({
    'http':'http://127..0.0.1:9743',
    'https':'http://127..0.0.1:9743'
})

opener = build_opener(proxy_handler)

try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)