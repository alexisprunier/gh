# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub import models
import urllib

class Facebook:
    def __init__(self,url,source,nb_infos):
        self.url = url
        self.source = source
        self.get_infos(nb_infos)
        
    def get_infos(self, nb_infos):
        
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
                
        list_art = page_web.find_all("item", limit=nb_infos)
        for article in list_art:
            content = title = news_link = None  

            try:       
                #link (wall or news ...)
                news_link = article.find("link").text
                split_wall_link = news_link.split('/',4)
                wall_link = "/".join(split_wall_link)
               
                #title
                title = (article.find("title")).text
                #Content
                content = article.find("description").text
                #BDD
                bdd_article = models.Facebook(titre=title,origine=self.source,contenu=content,lien=news_link)
                bdd_article.save()
            except:
                pass