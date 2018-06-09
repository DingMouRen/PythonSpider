from lxml import etree

'''
根据多个属性确定一个节点，可以使用运算符and来连接，
书籍页码p165,还有其他的运算符
'''
text = '''
<li class="li li-first" name="item"><a href="link.html">item1</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result)