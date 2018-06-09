from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">item1</a></li>
'''

html1 = etree.HTML(text)
result1 = html1.xpath('//li[@class="li"]/a/text()') # 属性有多个值，这种写法是匹配不到的
print(result1)
result2 = html1.xpath('//li[contains(@class,"li")]/a/text()') # 属性多值，通过contain()函数，参数1：属性名称 属性2：属性值
print(result2)