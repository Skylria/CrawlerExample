# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:09:26 2020

@author: juliana.m.venancio
"""
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Método para criação do crawler
def crawl(page):
    http = urllib3.PoolManager()
    try:
        data_page = http.request('GET', page)
    except:
        print('Page not found' + page)
        
    soup = BeautifulSoup(data_page.data)
    links = soup.find_all('a')
    cont = 1
    
    for link in links:
        #print(str(link.contents) + " - " + str(link.get('href')))
        print(link.attrs)
        print('\n')
        if('href' in link.attrs):
#concatena a url base com a url capturada
            url = urljoin(page, str(link.get('href')))
            if url != link.get('href'):
                print(url)
                print(link.get('href'))
            cont = cont + 1
        
    print (cont)    
crawl('https://pt.wikipedia.org/wiki/Linguagem_de_programação')
