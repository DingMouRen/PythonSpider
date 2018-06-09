from lxml import etree

html = etree.parse('./demo_1_test_节点轴.html',etree.HTMLParser())
# 1.ancestor轴获取所有祖先节点，::节点选择器，*表示匹配所有节点；此处返回第一个li节点的所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print('1.返回第一个li节点的所有祖先节点')
print(result)
# 2.返回祖先是div的节点
result = html.xpath('//li[1]/ancestor::div')
print('2.返回祖先是div的节点')
print(result)
# 3.attribute轴可以获取所有属性值，返回第一个li节点所有的属性值
result = html.xpath('//li[1]/attribute::*')
print('3.返回第一个li节点所有的属性值')
print(result)
# 4.child轴可以获取所有直接子节点，此处返回href属性是link1.html的a节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print('4.返回href属性是link1.html的a节点')
print(result)
# 5.descendand轴可以获取所有子孙节点，此处返回span节点
result = html.xpath('//li[1]/descendant::span')
print('5.返回span节点')
print(result)
# 6.following轴可以获取当前节点之后所有的节点，此处添加限定条件，只返回第二个后续节点
result = html.xpath('//li[1]/following::*[2]/text()')
print('6.此处添加限定条件，只返回第二个后续节点')
print(result)
# 7.following-sibling轴获取当前节点之后所有的同级节点，此处返回所有后续同级节点
result = html.xpath('//li[1]/following-sibling::*')
print('7.返回所有后续同级节点')
print(result)

