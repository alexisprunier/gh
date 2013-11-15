# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib


class Gizmodo :
    def __init__(self,nb_infos):
        self.url = 'http://www.gizmodo.fr/feed'
        self.source = "Gizmodo"
        self.get_infos(nb_infos)

        
    def get_infos(self, nb_infos):
    
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        #print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("item", limit=nb_infos)
        for article in list_art : 
                link = title = photo = date = None
                #link
                link = (article.find("link")).text
                #title
                title = ((article.find("title")).text).encode('utf-8')
                #photo
                try :
                    photo = article.find("media:content").get("url")
                except : pass   
                #BDD
                bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo)
                try :
                    bdd_article.save()
                except : pass                