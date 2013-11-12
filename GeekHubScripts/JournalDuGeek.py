# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib

class JournalDuGeek:
    def __init__(self,nb_infos):
        self.url = 'http://feeds2.feedburner.com/LeJournalduGeek'
        self.source = "Le Journal du Geek"
        self.get_infos(nb_infos)
    
    def get_infos(self, nb_infos):
        
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("item", limit=nb_infos)
        #print list_art #Affichage source complete #Affichege debug
        for article in list_art :    
                link = title = photo = None 
                #link
                link = (article.find("guid")).text
                #title
                title = (article.find("title")).text        
                #photo
                content = BeautifulSoup((article.find("content:encoded")).text)
                photo = content.find("img").get("src")
                #BDD
                bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
                try :
                    bdd_article.save()
                except : pass
                