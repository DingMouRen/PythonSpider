import http.cookiejar,urllib.request

'''
Cookies的处理
'''
# 1.以键值对的形式输出cookie信息
cookie = http.cookiejar.CookieJar() # 声明CookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler) # 建立一个opener
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name +'='+item.value)

'''
2.Cookies以文件形式保存
MozillaCookieJar是CookieJar的子类，用来处理Cookies与文件相关的事件，比如读取和保存Cookies,可以将Cookies保存成Mozilla
型浏览器的Cookies格式
'''
filename2 = 'cookies_mozilla.txt'
cookie2 = http.cookiejar.MozillaCookieJar(filename2)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener2 = urllib.request.build_opener(handler2)
response2 = opener2.open('http://www.baidu.com')
cookie2.save(ignore_discard=True,ignore_expires=True)

'''
3.Cookies以libwww-perl(LWP)格式保存成文件
'''
filename3 = 'cookies_lwp.txt'
cookie3 = http.cookiejar.LWPCookieJar(filename3)
handler3 = urllib.request.HTTPCookieProcessor(cookie3)
opener3 = urllib.request.build_opener(handler3)
response3 = opener3.open('http://www.baidu.com')
cookie3.save(ignore_discard=True,ignore_expires=True)