# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib
        
class Dealabs :
    def __init__(self,nb_infos):
        self.url = 'http://www.dealabs.com/2-hot.html'
        self.source = "Dealabs"
        self.get_infos(nb_infos)
    
    def get_infos(self, nb_infos):
        
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        #print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("article",{"class":"contenar"}, limit=5)
        print list_art.count()
        for article in list_art :    
            #link
            link = article.find("a", {"class":"voirledeal"}).get("href") 
            #title
            title =  article.find("p",{"style":";"}).text
            title = title.split
            final_title=None
            for i in range(0,title.length) :
                print title[i]
                
            #photo
            photo = (article.find("img",{"class":"image_defaut"})).get("src")
            #BDD
            print final_title
           
            '''bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
            try :
                bdd_article.save()
            except : pass'''