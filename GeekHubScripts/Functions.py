# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from GeekHub.models import Article
import urllib2
from GeekHub import bitly


def getNewsArticles(source,nb_infos) :
    articles = []        
    i = 0
    while i<10:
        try:
            page = urllib2.urlopen(source)
        except:
            i += 1
            continue
        break
    html = page.read()
    page_web = BeautifulSoup(html)
    
    list_art = page_web.find_all("item", limit=nb_infos)
    
    for article in list_art :
        link = (article.find("guid")).text
        print link
        articles.append(link)
    return articles   
        
def saveNews(source, link, bit_login, bit_apikey):
    image = title = bit_link = None
    i = 0
    while i<10:
        try:
            page = urllib2.urlopen(link)
        except:
            i += 1
            continue
        break
    html = page.read()
    page_web = BeautifulSoup(html)

    try :
        image = page_web.find("meta", {"property":'og:image'}).get("content")
    except :
        pass
    if image == None or "icon" in image :
        images = page_web.find_all("img")
        for img in images :
            if "logo" not in img and "icon" not in img:
                image = img.get("src")
                break    
    print image
    
    try :
        title = page_web.find("meta", {"property":'og:title'}).get("content")
    except : pass 
    if title == None :
        title = page_web.find("title").text
    print title.encode("utf-8")
     
    #Bitly
    api = bitly.Api(login=bit_login, apikey=bit_apikey)
    print link
    bit_link = api.shorten(link)
     
    
    article = Article(titre=title,origine=source,lien=link, short_link = bit_link, image = image )
    article.save()
    