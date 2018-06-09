from lxml import etree

# 1.匹配所有节点
html1 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result1 = html1.xpath('//*') # *表示匹配所有节点，返回一个列表，每一个元素都是Element类型，其后是节点的名称，html,body等
print('1.匹配所有节点')
print(result1)

# 2.匹配指点节点名称
html2 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result2 = html2.xpath('//li')
print('2.匹配指点节点名称')
print(result2)
print(result2[0])
