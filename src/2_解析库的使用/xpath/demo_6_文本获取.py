from lxml import etree

'''
文本获取
'''
# 1.先选取到特定的子孙节点，再调用text()函数选取其内部文本，这样可以保证获取的结果是整洁的
html1 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result1 = html1.xpath('//li[@class="item-0"]/a/text()') # /表示获取直接子节点
print('1.先选取到特定的子孙节点，再调用text()函数选取其内部文本，这样可以保证获取的结果是整洁的')
print(result1)

# 2.//加text()函数获取子孙节点内部所有的文本，可以保证获取最全面的文本信息，但是可能夹杂一些换行符等特殊符号
html2 = etree.parse('./demo_1_test.html',etree.HTMLParser())
result2 = html2.xpath('//li[@class="item-0"]//text()') # /表示获取直接子节点
print('2.//加text()函数获取子孙节点内部所有的文本，可以保证获取最全面的文本信息，但是可能夹杂一些换行符等特殊符号')
print(result2)


