from lxml import etree

html1 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result1 = html1.xpath('//li/a') # //li/a表示查找所有li节点的所有直接子节点a
print(result1)