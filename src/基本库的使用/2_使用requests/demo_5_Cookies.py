import requests

'''
Cookies处理

'''
response = requests.get('https://www.baidu.com')
print(type(response.cookies),type(response.cookies.items()),sep='\n')
print(response.cookies)
for key,value in response.cookies.items():
    print(key+'='+value)

# Cookie添加到Headers中，然后发送请求
headers = {
    'Cookie':'_zap=a987f09d-04cb-47e8-82f4-ad341eaa6b54; d_c0="ACBC7LuLQAyPTrYXDhbMceYoUenpjQbMFcI=|1503270027"; q_c1=a3b968c8081e45cdaea844f1ba63f447|1505639063000|1497439580000; __utma=51854390.746573005.1511308133.1512354730.1516416787.5; __utmz=51854390.1516416787.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20170614=1; z_c0="2|1:0|10:1517010352|4:z_c0|92:Mi4xbTZyQkF3QUFBQUFBSUVMc3U0dEFEQ1lBQUFCZ0FsVk5zQXRaV3dEYlZGeElybnc2UFJaVkx4ZFdEb2p6V0VhUjlB|ba037aa2a542cae174c219271d2f664ef69def543bdc745fdfc1fdb8fd23133e"; __DAYU_PP=eAANJeuenzy2neQMuffb2bf92b4ba89f; q_c1=a3b968c8081e45cdaea844f1ba63f447|1525879717000|1497439580000; __lnkrntdmcvrd=-1; _xsrf=cf737535-cd50-4610-b414-d23e8b5a481c; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
response_2 = requests.get('https://www.zhihu.com',headers=headers)
print(response_2.status_code,response_2.text,sep='\n')