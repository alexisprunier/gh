# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib2
from GeekHub import bitly
        
class ZeroUnnet :
    def __init__(self,nb_infos, bit_login, bit_apikey):
        self.url = 'http://www.01net.com/rub/actualites/10001/'
        self.source = "01net"
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
        
        #print page_web.prettify() #Affichage source complete
        
        list_art = page_web.find_all("div",{"class":"Actu_Box"}, limit=nb_infos)
        for article in list_art :    
            #link
            link = (article.find("h2")).find("a").get("href") 
            #title
            title =  (article.find("h2")).find("a").text     
            #photo
            photo = (article.find("img",{"class":"lazy"})).get("data-original")
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
