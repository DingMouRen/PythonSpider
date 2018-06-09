from lxml import etree

'''
获取所有li节点下所有a节点的href属性
@href表示获取节点的href属性
[@href="link2.html"]表示属性匹配
'''
html = etree.parse('./demo_1_test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)