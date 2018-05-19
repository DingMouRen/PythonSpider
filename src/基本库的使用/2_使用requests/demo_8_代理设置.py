import requests
'''
代理设置的示例代码,无效代码哦，也支持SOCKS协议代理，需要去下载包看书136页
'''
proxy_ips = {
    'http':'http://10.10.1.10:3128',
    'https':'http://10.10.1.10:1080'
}
requests.get('https://www.taobao.com',proxies=proxy_ips)
