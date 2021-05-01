import requests
import re
import os
search = ['招聘','投稿','上传','举报','在线投稿','联系我们','上传文件']#敏感字符
searchNum = len(search)
num=0                 #while循环初始
url="http://"+input("请输入网址")   #网址
url1=requests.get(url)              #get网址
url2=url1.text                      #url2为源代码
while True:                         #循环
    search1=search[num]                #search1为敏感字符中的元素
    a=re.search(search1, url2, flags=0) #正则表达式，查看url2是否有search1的字符，flag为正则表达式的模式
    num+=1                              #查询完毕更换下一个敏感字符                          #输出查找到的敏感字符的位置
    if a!=None:
        print("查找到敏感字符",search1,"可能存在文件上传漏洞")
    else:
        print("未查到敏感字符，可能不存在上传点或需要手动查找")
    if num==searchNum:                            #结束循环
        break

os.system("pause")