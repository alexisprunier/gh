# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from GeekHub.models import Article
import urllib

url = 'http://www.comptoir-hardware.com/home.xml'
source = "Le Comptoir du Harware"



html = urllib.urlopen(url).read()
page_web = BeautifulSoup(html)

print page_web.prettify() #Affichage source complete

list_art = page_web.find_all("item", limit=10)
for article in list_art :    
        #link
        link = (article.find("guid")).text
        #title
        title = (article.find("title")).text        
        #photo
        photo = article.find("enclosure").get("url")
        #BDD
        #bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
        #bdd_article.save()
        print link
        print title
        print photo