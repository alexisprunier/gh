# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib

list_extension = ["png","jpeg", "jpg", "gif"]
class FrAndroid :
    def __init__(self,nb_infos):
        self.url = 'http://feedpress.me/frandroid'
        self.source = "FrAndroid"
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
                content_html = article.find("content:encoded").text
                content = BeautifulSoup(content_html) 
                try :
                    photo = content.find("img").get("src")
                    type_fic = photo.split('.')[-1]
                    if type_fic not in list_extension :
                        photo = None 
                except : pass  
                #BDD
                bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo)
                try :
                    bdd_article.save()
                except : pass           