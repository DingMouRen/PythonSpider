from lxml import etree

'''
@符号进行属性过滤
'''
html = etree.parse('./demo_1_test.html',etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)
