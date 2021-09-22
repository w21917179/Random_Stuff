# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 00:22:55 2021

@author: Owner

esj爬蟲，link填入第一話，之後會自己找下一話

"""

import requests
from bs4 import BeautifulSoup
from sys import exit

link = 'https://www.esjzone.cc/forum/1551091950/48945.html'

while(True):
    response = requests.get(link)
    #print(response.text)
    
    soup = BeautifulSoup(response.text, "lxml")
    #print(soup.prettify())  #輸出排版後的HTML內容
    
    titles = soup.find('h2')
    print(titles.get_text())
    
    article = soup.find(class_='forum-content mt-3')
    #print(article)
    
    with open('index.txt', 'a+', encoding='UTF-8') as file:
        file.write(titles.get_text())
        file.write('\n')
        file.write(article.get_text())
        file.write('\n')
        
    
    try:
        link = soup.find(class_='btn btn-outline-secondary btn-sm btn-next').get('href')
        print(link)
    except AttributeError:
        print('大概沒了')
        exit(0)
