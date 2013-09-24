# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from GeekHub.models import Article
import urllib

url = 'http://www.presse-citron.net/'
source = "Presse Citron"



html = urllib.urlopen(url).read()
page_web = BeautifulSoup(html)


page_web = page_web.find("div", {"class":"posts posts-index"}) #Nettoyage, selection de la div des posts

#print page_web.prettify() #Affichage source complete
list_art = page_web.find_all("div",{"class":"hentry"}, limit=10)
print list_art
for article in list_art :    
        #link
        link = (article.find("h2", {"class":"post-title"})).find("a").get("href")  
        #title
        title =  (article.find("h2", {"class":"post-title"})).find("a").text  
        print title   
        #photo
        photo = (article.find("p",{"class":"post-thumbnail"})).find("img").get("src")
        #BDD
        #bdd_article = Article(titre = title, lien = link, origine = self.source, image = photo )
        #bdd_article.save()
        print link
       
        print photo