from lxml import etree
'''
匹配父节点
'''
# 1.匹配父节点
html1 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result1 = html1.xpath('//a[@href="link4.html"]/../@class')
print('1.匹配父节点')
print(result1)

# 2.匹配父节点 parent
html2 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result2 = html2.xpath('//a[@href="link4.html"]/parent::*/@class') #parent::获取父节点
print('2.匹配父节点 parent')
print(result2)