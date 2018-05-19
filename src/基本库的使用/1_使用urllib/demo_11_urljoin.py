from urllib.parse import urljoin

'''
urljoin()函数可以实现链接的解析 拼合与生成，可以生成新的URL
urljoin()有两个参数：第一个参数是个基础链接，第二个参数是新的链接。
该方法会分析基础链接的scheme netloc path三部分内容，新连接对缺失的部分进行补充，
如果基础链接中存在，会使用新的链接的内容部分，基础链接中的params query和fragment会被忽略掉

https://www.cuiqingcai.com/index.html?name=jack#comment
'''

url1 = 'http://www.baidu.com?id=6'
url2 = 'https://www.cuiqingcai.com/index.html?name=jack#comment'
result = urljoin(url1,url2)
print(result)