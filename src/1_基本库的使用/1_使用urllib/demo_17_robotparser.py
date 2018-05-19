from urllib.robotparser import RobotFileParser
from urllib import request
from urllib.error import URLError
'''
RobotFileParser类用来判断网站是否可以被抓取
可以直接在声明时传入链接，urllib.robotparser.RobotFileParser(url=''),也可以在后面通过set_url()函数来设置
常用方法说明：
set_url():用来设置robots.txt文件的链接
read():读取tobots.txt文件并进行分析。此方法执行拂去和分析操作，不返回任何内容，必须调用此方法，否则后面的操作都返回false
parse():用来解析robots.txt文件传入的参数是robots.txt某些行的内容，按照robots.txt语法规则进行分析
can_fetch():返回是否可以抓取这个URL，True或False,参数：User-agent  ,要抓取的URL
mtime():f返回的是上次抓取和分析robots.txt的时间，可以定期检查来抓取最新的robots.txt
modified()：可以将当前时间设置为上次抓取和分析robots.txt的时间

都不能爬取，不晓得怎么回事😔
'''
robotFileParser = RobotFileParser()
robotFileParser.set_url('https://www.jianshu.com/robots.txt')
robotFileParser.read() # 对robots.txt文件进行读取和分析，必须调用
print('read()函数解析')
print(robotFileParser.can_fetch('*','https://www.jianshu.com/p/2af3cb3c05f2'))
print(robotFileParser.can_fetch('*','https://www.jianshu.com/search?q=android%20%E8%BD%AF%E9%94%AE%E7%9B%98&page=1&type=note'))

robotFileParser1 = RobotFileParser()
url = 'https://www.jianshu.com/robots.txt'
userAgent = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
headers = {
    'User-Agent' : 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
req = request.Request(url=url,headers=headers)
response = request.urlopen(req)
robotFileParser1.parse(response.read().decode('utf-8').split('\n'))
print('parse()函数解析')
print(robotFileParser.can_fetch('Googlebot','https://www.jianshu.com/p/2af3cb3c05f2'))
print(robotFileParser.can_fetch('Googlebot','https://www.jianshu.com/search?q=android%20%E8%BD%AF%E9%94%AE%E7%9B%98&page=1&type=note'))

