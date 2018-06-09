from lxml import etree

'''
有时候，在选择的时候某些属性可能匹配到多个节点，我们只想要其中的某个节点，或者其他节点
索引从1开始的，注意，
其他函数处理参考：http://www.w3school.com.cn/xpath/xpath_functions.asp
'''
html = etree.parse('./demo_1_test.html',etree.HTMLParser())
result = html.xpath('//li[1]/a/text()') # 第一个
print(result)
result = html.xpath('//li[last()]/a/text()') # 最后一个
print(result)
result = html.xpath('//li[position()<3]/a/text()') # 第一个 第二个
print(result)
result = html.xpath('//li[last()-2]/a/text()') # 倒数第三个
print(result)