import requests
import re
import os
searchword = ['招聘',
              '投稿',
              '上传',
              '举报',
              '在线投稿',
              '联系我们',
              '上传文件']#敏感字符
searchfunction=['<INPUT TYPE="file"',
                '<input type="file"',
                'INPUT TYPE="FILE"']

searchwordNum = len(searchword)
searchNum2 =len(searchfunction)
url="http://"+input("请输入网址")
url1=requests.get(url)
url2=url1.text


def word():     #敏感字符查找
    num=0
    while True:
        searchword1=searchword[num]
        a=re.search(searchword1, url2, flags=0) #正则表达式，查看url2是否有search1的字符，flag为正则表达式的模式
        num+=1                              #查询完毕更换下一个敏感字符
        if a!=None:
            print("\033[34m查找到敏感字符",searchword1,"可能存在文件上传漏洞\033[0m")
        else:
            pass
        if num==searchwordNum:                            #结束循环
            num=0
            break

def function(): #敏感函数查找
    num=0
    while True:
        searchfunction1 = searchfunction[num]  #searchfunction为敏感函数
        b = re.search(searchfunction1, url2, flags=0)  # 正则表达式
        num += 1
        if b != None:
            print("\033[34m查找到敏感函数", searchfunction1, "可能存在文件上传漏洞\033[0m")
        else:
            pass
        if num == searchNum2:  # 结束循环
            break

word()
function()
print("\033[31m如果没有回显就是暂未查到文件上传，网站没有或需要手动搜索\033[0m")
print("\033[31m注意，敏感函数扫描需要转换一下大小写，转成小写的然后去网站审查元素直接定位就好\033[0m")
os.system("pause")