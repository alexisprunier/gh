# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib2
from GeekHub import bitly

class PresseCitron :
    def __init__(self,nb_infos, bit_login, bit_apikey):
        self.url = 'http://www.presse-citron.net/'
        self.source = "Presse Citron"
        self.get_infos(nb_infos, bit_login, bit_apikey)
        
    def get_infos(self, nb_infos, bit_login, bit_apikey):
    
        while True:
            try:
                page = urllib2.urlopen(self.url, timeout=10)
            except:
                continue
            break
        html = page.read()
        page_web = BeautifulSoup(html)
        
        page_web = page_web.find("div", {"class":"posts posts-index"}) #Nettoyage, selection de la div des posts
        list_art = page_web.find_all("div",{"class":"hentry"}, limit=nb_infos)
        for article in list_art :
            link = title = photo = date = None
            #link
            link = (article.find("h2", {"class":"post-title"})).find("a").get("href")  
            #title
            title =  (article.find("h2", {"class":"post-title"})).find("a").text
            title = title.replace('&apos;',"'")  
            #photo
            photo = (article.find("p",{"class":"post-thumbnail"})).find("img").get("src")
            #Bitly
            api = bitly.Api(login=bit_login, apikey=bit_apikey)
            while True :
                try:
                    bit_link = api.shorten(link)
                except:
                    continue
                break
            #BDD
            bdd_article = Article(titre = title, lien = link, short_link = bit_link, origine = self.source, image = photo)
            try :
                bdd_article.save()
            except : pass
        page.close()

