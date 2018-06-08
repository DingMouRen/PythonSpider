import requests
import json
from requests.exceptions import RequestException
import re
import time

# 抓取html的内容
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
        }
        reponse = requests.get(url,headers=headers)
        if reponse.status_code == 200:
            return reponse.text
        return None
    except RequestException:
        return None

# 解析抓取到的html内容
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{ #yield是生成器
            'index':item[0],
            'image':items[1],
            'title':item[2],
            'actor':item[3].strip()[3:],  # strip()去除前后的空格，[3:]获取位置从3开始到结尾的字符串
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

# 将解析好的内容写入文件
def write_to_file(content):
    with open('猫眼电影排行.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

# 分页爬取
def main(offset):
    url = 'http://maoyan.com/board/4?offsset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)