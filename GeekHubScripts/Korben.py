# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib


class Korben :
    def __init__(self,nb_infos):
        self.url = 'http://feeds.feedburner.com/KorbensBlog-UpgradeYourMind?format=xml'
        self.source = "Korben"
        self.get_infos(nb_infos)

        
    def get_infos(self, nb_infos):
    
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        #print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("item", limit=nb_infos)
        for article in list_art : 
                link = title = photo = date = None
                #link
                link = (article.find("feedburner:origlink")).text
                #title
                title = ((article.find("title")).text).encode('utf-8')
                #photo
                
                content= article.find('content:encoded').text
                content_html = BeautifulSoup(content)
                photo = content_html.find('img').get("src")
            
                #BDD
                bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo)
                try :
                    bdd_article.save()
                except : pass                