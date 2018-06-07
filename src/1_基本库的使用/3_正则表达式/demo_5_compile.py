import re

'''
compile()将正则字符串编译成正则表达式对象
'''
content1 = '2018-12-15 12:00'
content2 = '2018-12-16 12:20'
content3 = '2018-12-25 14:00'
pattern = re.compile('\d{2}:\d{2}')
print(re.search(pattern,content1).group())
print(re.search(pattern,content2).group())
print(re.search(pattern,content3).group())