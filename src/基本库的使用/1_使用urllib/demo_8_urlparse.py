from urllib.parse import urlparse
'''
urlparse()函数可以实现URL的识别的分段，返回ParseResult对象，包含6部分内容

http://www.baidu.com/index.html;user?id=5#comment
解析结果：
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
scheme:表示协议
netloc:表示域名
path:表示访问路径
params:表示参数
query:表示查询条件
fragment:表示锚点

urllib.parse.urlparse(urlstring,scheme='',allow_fragment=True)
urlstring:待解析的URL,必填
scheme:表示默认协议，只有在URL中不包含协议信息时才有作用
allow_fragment:表示是否忽略fragment,

'''
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')

result1  = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='http',allow_fragments=False)
print(result1)