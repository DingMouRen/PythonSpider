from urllib.parse import parse_qsl

'''
parse_qsl()函数将参数转化成元组组成的列表
[('id', '666'), ('name', 'jack'), ('age', '18')]
'''
query = 'id=666&name=jack&age=18'
result = parse_qsl(query)
print(result)