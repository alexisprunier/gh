# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib

class PresseCitron :
    def __init__(self,nb_infos):
        self.url = 'http://www.presse-citron.net/'
        self.source = "Presse Citron"
        self.get_infos(nb_infos)

        
    def get_infos(self, nb_infos):
    
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        page_web = page_web.find("div", {"class":"posts posts-index"}) #Nettoyage, selection de la div des posts
        list_art = page_web.find_all("div",{"class":"hentry"}, limit=nb_infos)
        for article in list_art :    
            #link
            link = (article.find("h2", {"class":"post-title"})).find("a").get("href")  
            #title
            title =  (article.find("h2", {"class":"post-title"})).find("a").text  
            #photo
            photo = (article.find("p",{"class":"post-thumbnail"})).find("img").get("src")

            #BDD
            bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
            try :
                bdd_article.save()
            except : pass
