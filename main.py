import subprocess
import os
import lxml
def zac():
    print("\033[31m----------------------------------\033[0m")
    print("\033[31m ZAC漏洞扫描器\033[0m")
    print("\033[31m公众号：ZAC安全\033[0m")
    print("\033[31m个人微信号: shenfenxinxichaxun99\033[0m")
    print("\033[31murl格式为 www.xxxxxxxx.xxxx\033[0m")
    print("\033[31m----------------------------------\033[0m")
zac()

print("1 漏洞扫描器",
      "2 文件上传扫描",
      "3 获取当前网站下所有连接",
      "4 xss扫描")
a = int(input("请输入你需要使用的扫描器编号"))

if a==1:
    os.system('scan.py')
    exit()
elif a==2:
    os.system('uploadscan.py')
    exit()
elif a==3:
    os.system('linksearch.py')
elif a==4:
    os.system('xssscan.py')


