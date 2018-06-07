import re

'''
sub()函数可以用来修改文本，replace()函数太繁琐，
html文本也可以这么处理
'''
content1 = "234hh2345hgg7hh43lhh"
content_result = re.sub('\d+','',content1)  #去除数字
print(content_result)