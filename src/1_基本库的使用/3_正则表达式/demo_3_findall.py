import re

'''
findall()函数会搜索整个字符串，返回匹配正则表达式的所有内容
获取多个内容，用findall()函数
'''
content1 = '''<!DOCTYPE html>
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
    <a href="4.mp3" singer="刘若英">后来</a>
</li>
</body>
</html>'''
rule = '<li.*?singer="(.*?)">(.*?)</a>'
results = re.findall(rule,content1,re.S)
print(results)
for result in results: # results是一个列表，result是一个元组
    print(result[0],result[1],sep=":")