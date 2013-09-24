# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from GeekHub.models import Article
import urllib

url = 'http://www.01net.com/rub/actualites/10001/'
source = "01net"



html = urllib.urlopen(url).read()
page_web = BeautifulSoup(html)

#print page_web.prettify() #Affichage source complete

list_art = page_web.find_all("div",{"class":"Actu_Box"}, limit=10)
for article in list_art :    
        #link
        link = (article.find("h2")).find("a").get("href") 
        #title
        title =  (article.find("h2")).find("a").text     
        #photo
        photo = (article.find("img",{"class":"lazy"})).get("data-original")
        #BDD
        #bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
        #bdd_article.save()
        print link
        print title
        print photo