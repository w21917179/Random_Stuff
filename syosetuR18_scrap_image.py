'''
>>> jar = requests.cookies.RequestsCookieJar()
>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
>>> url = 'https://httpbin.org/cookies'
>>> r = requests.get(url, cookies=jar)

小說家(R18)爬蟲，把圖片爬出來


'''


import requests
import urllib.request
from bs4 import BeautifulSoup
from sys import exit

link = 'https://novel18.syosetu.com/n2251fl/'
i = 1
headers = {'user-agent': 'my-app/0.0.1'}
jar = requests.cookies.RequestsCookieJar()
jar.set('over18', 'yes', domain='.syosetu.com', path='/')

srcurl = ['https://static.syosetu.com/novelview/img/novelview_on.gif?n7nper','https://static.syosetu.com/novelview/img/Twitter_logo_blue.png?nrkioy', 'https://static.syosetu.com/novelview/img/novelview_on.gif?n7nper']

# 計算章節數量
para = link.replace('https://novel18.syosetu.com', '')  #取網址後面的參數
chapter = 0  #記錄小說章節數量
response = requests.get(link, headers=headers, cookies=jar)
soup = BeautifulSoup(response.text, "lxml")
url = soup.find_all('a')  #找所有網址
for i in url:
    if (i.get('href').find(para, 0, 9) >= 0 ):
        temp = i.get('href').replace(para,'').replace('/','')  #刪除參數和斜線，取出數字
        #print(temp)  
        chapter = max(chapter, int(temp))  #記錄當前最大章節

print(chapter)



for n in range(1,chapter+1):
    print(link+ str(n)+ '/')
    response = requests.get(link+ str(n)+ '/', headers=headers, cookies=jar)    #link+ str(i)+ '/'
    #print(response.status_code)
    
    soup = BeautifulSoup(response.text, "lxml")
    #print(soup.prettify())  #輸出排版後的HTML內容
    
    titles = soup.find_all('img')
    
    for i in titles:
        isrc = i.get('src')
        
        if ((isrc in srcurl) == False):
            with open('index100.txt', 'a+', encoding='UTF-8') as file:
                print(i)
                file.write(str(i))
                file.write('\n')

    