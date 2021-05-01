import requests
import re
from lxml import etree
import os
                 #while循环初始
link = input("你需要查找的网站")
url="http://"+link
url1=requests.get(url)              #get网址
url2=url1.text
html=etree.HTML(url2)
print("1 获得网页下全部的连接")
print("2 获得前缀不是www的连接")
linksearch = int(input("你需要得到的连接"))

def all():
    zac=html.xpath('//a/@href')
    str = '\n'
    f = open("all.txt", "w")
    f.write(str.join(zac))
    f.close()

def Prefix():
    zac = html.xpath('//a/@href')
    prefix=[]
    for i in zac:
        a = i[0:10]
        b = i[0]
        if a!="http://www" and b !="." and b!="#":
            prefix.append(i)
    str = '\n'
    f = open("pre.txt", "w")
    f.write(str.join(prefix))
    f.close()


if linksearch==1:
    all()
elif linksearch==2:
    Prefix()
os.system("pause")


