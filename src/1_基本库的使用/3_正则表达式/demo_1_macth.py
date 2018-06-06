import re
'''
match()函数会从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果，如果不匹配，就返回None
'''
# 1.match()函数的基本使用
content1 = 'Hello 123 4567 World_This is a Regex Demo'
print("原字符串：",content1)
result1 = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content1) # 第一个参数：正则表达式  第二个参数：需要匹配的字符串
print("1.match()函数的基本使用")
print(len(content1))
print(result1)
# print(result1.group()) #  group()函数输出匹配到的内容
print(result1.span())  #  span()函数输出匹配的范围，也就是匹配到的字符串在原字符串中的位置范围

# 2.匹配目标  用()标记一个子表达式的开始和结束位置，被标记的每个子表达式会一次对应一个分组，索引从1开始，group(1)
content2 = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\sWorld',content2)
print("2.匹配目标")
print(result2)
print(result2.group())
print(result2.group(1)) # group(1)会输出第一个被正则表达式中第一个被()包围的匹配结果，如果正则表达式后面还有()，依次是group(2)..
print(result2.span())

# 3.通用匹配 .和*,点可以匹配除换行符之外的任意字符，*表示匹配前面的字符无限次,可以用来简化正则表达式的书写
content3 = 'Hello 123 4567 World_This is a Regex Demo'
result3 =  re.match('^Hello.*World',content3)
print("3.通用匹配")
print(result3)
print(result3.group())
print(result3.span())

# 4.贪婪与非贪婪
'''
贪婪匹配：.*这是贪婪匹配的写法，会尽可能匹配多的字符
非贪婪匹配：.*?这是非贪婪匹配的写法，会尽可能匹配少的字符
注意：
1.目标字符串在中间的话，尽量使用非贪婪匹配，以免出现匹配结果却是的情况
2.目标字符串出现在末尾的话，使用非贪婪匹配很有可能匹配不到内容，因为它会匹配尽量少的字符
'''
content4 = 'Hello 1234567 World_This is a Regex Demo'
result4_1 = re.match('^He.*(\d+).*Demo$',content4)
result4_2 = re.match('^He.*?(\d+).*Demo$',content4)
print('4.贪婪与非贪婪')
print('贪婪匹配:',result4_1.group(1))
print('非贪婪匹配:',result4_2.group(1))

# 5.修饰符
'''
这个例子中有一个换行符，没有re.S的话就匹配不到字符串
修饰符：
re.I:使匹配对大小写不敏感(网页匹配中常用)
re.L:做本地化识别匹配(locale-aware)
re.M:多行匹配，影响^和$
re.S:使.点匹配包括换行在内的所有字符(网页匹配中常用)
re.U:根据Unicode字符集解析字符。这个标志影响 \w \W \b \B
re.X:该标志通过给予你更灵活的格式以便你将正则表达式写的更易于理解  
'''
content5 = 'Hello 1234567 World_This \n is a Regex Demo'
result5 = re.match('^He.*?(\d+).*?Demo$',content5,re.S)
print("5.修饰符")
print(result5)
print(result5.group(1))
print(result5.span())

# 6.转义匹配   当遇到用于正则匹配模式的特殊字符时，在前面加反斜线转义一下

content6 = '(百度)www.baidu.com'
result6 = re.match('\(百度\)www\.baidu\.com',content6)
print('6.转义匹配')
print(result6)
print(result6.group())