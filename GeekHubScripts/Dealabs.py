# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib2
        
class Dealabs :
    def __init__(self,nb_infos, bit_login, bit_apikey):
        self.url = 'http://www.dealabs.com/2-hot.html'
        self.source = "Dealabs"
        self.get_infos(nb_infos, bit_login, bit_apikey)
    
    def get_infos(self, nb_infos, bit_login, bit_apikey):
        
        while True:
            try:
                page = urllib2.urlopen(self.url, timeout=10)
            except:
                continue
            break
        html = page.read()
        
        
        #page_web = str(html).replace("article","div")
        
        
        f1=open('test_dealabs.txt','w+')
        f1.write(str(html))
        f1.close()
        #print page_web.prettify() #Affichage source complete
        
        list_art = soup.findAll("div",{"class":"contenar"})
        print len(list_art)
        for article in list_art :  
            
            #link
            link = article.find("div", {"class":"contenar-heading"}).contents[3].get("href")
            print link 
            #title
            title =  article.find("div", {"class":"contenar-heading"}).contents[3].text
            #Remove SPACE before and after
            title = title.lstrip().rstrip()
            print title
            #photo
            photo = (article.find("img",{"class":"image_defaut"})).get("src")
            print photo
            #Bitly
            
            #BDD
           
            '''bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
            try :
                bdd_article.save()
            except : pass'''
        page.close()
