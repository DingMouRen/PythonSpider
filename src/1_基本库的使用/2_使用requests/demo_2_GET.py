import requests
from urllib.error import URLError
import re

# 1.基本使用
try:
    response_1 = requests.get('http://httpbin.org/get')
except URLError as e:
    print(e.reason)
print('get基本使用:',response_1.text,sep='\n')

# 2.添加参数
data_2 = {
    'id':'1',
    'name':'jack',
    'age':'18'
}
response_2 = requests.get('http://httpbin.org/get',params=data_2)
print('get添加参数:',response_2.text,sep='\n')

# 3.返回是json格式的话，我们可以将json转换成字典格式完成解析,Response对象的json函数可以将Json转换成字典格式
response_3 = requests.get('http://httpbin.org/get')
print('get的json解析:',response_3.json(),type(response_3.json()),sep='\n')

# 4.抓取网页与添加Headers
headers_4 = {
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
response_4 = requests.get('https://www.zhihu.com/explore',headers=headers_4) # User-Agent字段信息是浏览器标识信息，模拟浏览器请求，知乎会禁止抓取
pattern_4 = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles_4 = re.findall(pattern_4,response_4.text)
print(titles_4)

# 5.抓取二进制数据
response_5 = requests.get('https://github.com/favicon.ico')
print(response_5.text) # 这里是将图片转化成字符串类型，就会出现乱码
print(response_5.content) # 输出bytes类型数据
with open('favicon.ico','wb') as file:  # open函数：第一个参数文件名称，第二个参数以二进制写的形式打开
    print(type(file)) # file类型是<class '_io.BufferedWriter'>
    file.write(response_5.content)

# 6.