# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib2
from GeekHub import bitly

class Hardware :
    def __init__(self,nb_infos, bit_login, bit_apikey):
        self.url = 'http://feeds.feedburner.com/hardware/fr/news/'
        self.source = "Hardware.fr"
        self.get_infos(nb_infos, bit_login, bit_apikey)
        
    def get_infos(self, nb_infos, bit_login, bit_apikey):
    
        i = 0
        while i<10:
            try:
                page = urllib2.urlopen(self.url, timeout=10)
            except:
                i += 1
                continue
            break
        html = page.read()
        page_web = BeautifulSoup(html)
        
        #print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("item", limit=nb_infos)
        for article in list_art :    
            link = title = photo = date = None
            #link
            link = (article.find("guid")).text
            #title
            title = (article.find("title")).text        
            #photo
            try :
                photo = article.find("enclosure").get("url")
            except : photo = ""
            #Bitly
            api = bitly.Api(login=bit_login, apikey=bit_apikey)
            i = 0 
            while i<10 :
                try:
                    bit_link = api.shorten(link)
                except:
                    i += 1
                    continue
                break
            #BDD
            bdd_article = Article(titre = title, lien = link, short_link = bit_link, origine = self.source, image = photo)
            try :
                bdd_article.save()
            except : pass    
        page.close()
            