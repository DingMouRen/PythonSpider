import re

'''
search()函数会扫描整个字符串，然后返回第一个成功匹配的结果，如果没有符合的就返回None.正则表达式可以是字符串的一部分
'''
# 1.search()基本使用
content1 = "Hello from your'friend"
result1_match = re.match('your',content1)
result1_search = re.search('your',content1)
print('match匹配结果:',result1_match)
print('search匹配结果:',result1_search)

# 2.提取html中的字符串
content2 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<li data-view="1" class="active">
    <a href="4.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="1">
    <a href="4.mp3" singer="齐秦">往事随风</a>
</li>
</body>
</html>'''
rule = '<li.*?active.*singer="(.*?)">(.*?)</a>'
result2 = re.search(rule,content2,re.S)
print(result2)
if result2:
    print(result2.group(1),result2.group(2),sep=':')