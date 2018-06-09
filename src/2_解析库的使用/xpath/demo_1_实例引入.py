from lxml import etree

# 1.解析html的文本
text1 = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">item1</a></li>
        <li class="item-1"><a href="link2.html">item2</a></li>
        <li class="item-inactive"><a href="link3.html">item3</a></li>
        <li class="item-1"><a href="link4html">item4</a></li>
        <li class="item-0"><a href="link5html">item5</a>
    </ul>
</div>
'''
html1 = etree.HTML(text1) # 初始化，构造xpath解析对象,最后一个li节点没有闭合，etree模块会自动修正html文本
result1 = etree.tostring(html1) # 输出修正后的Html文本,但是输出的是bytes类型，decode()函数将bytes转换成str类型
print('1.解析html的文本')
print(type(result1))
print(result1.decode('utf-8'))

# 2.解析html的文本文件
html2 = etree.parse('./demo_1_test.html',etree.HTMLParser()) # 初始化，构造xpath解析对象,最后一个li节点没有闭合，etree模块会自动修正html文本
result2 = etree.tostring(html2) # 输出修正后的Html文本,但是输出的是bytes类型，decode()函数将bytes转换成str类型
print('2.解析html的文本文件')
print(type(result2))
print(result2.decode('utf-8'))