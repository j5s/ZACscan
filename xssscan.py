import requests
import re
import os
#敏感字符
searchWord = [
          '投稿',
          '上传',
          '举报',
          '在线投稿',
          '联系我们',
          '简介',
          '昵称',
          '搜索']
#敏感函数
searchFunction=['<INPUT TYPE="TEXT"',
                '<input type="text"',
                '<INPUT TYPE="CONTENT"',
                '<input type="content"',
                '<input type="submit"',
                'INPUT TYPE="SUBMIT"'
                ]
searchWordNum = len(searchWord)
searchFunctionNum =len(searchFunction)

url="http://"+input("请输入网址")
url1=requests.get(url)
url2=url1.text



def word():     #敏感字符
    num=0
    while True:
        searchWord1=searchWord[num]
        a=re.search(searchWord1, url2, flags=0) #正则表达式，查看url2是否有search1的字符，flag为正则表达式的模式
        num+=1                              #查询完毕更换下一个敏感字符
        if a!=None:
            print("\033[34m查找到敏感字符",searchWord1,"可能存在XSS\033[0m")
        else:
            pass
        if num==searchWordNum:                            #结束循环
            num=0
            break

def function(): #敏感函数
    num=0
    while True:
        searchFunction1 = searchFunction[num]  #searchfunction为敏感函数
        b = re.search(searchFunction1, url2, flags=0)  # 正则表达式
        num += 1
        if b != None:
            print("\033[34m查找到敏感函数", searchFunction1, "可能存在XSS\033[0m")
        else:
            pass
        if num == searchFunctionNum:  # 结束循环
            break

word()
function()

