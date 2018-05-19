from urllib.parse import parse_qs

'''
反序列化，将GET请求参数转换成字典
{'id': ['666'], 'name': ['jack'], 'age': ['18']}
'''
query = 'id=666&name=jack&age=18'
result = parse_qs(query)
print(result)