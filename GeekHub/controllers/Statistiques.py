#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.controllers.Proxy import Proxy
from GeekHub.models import Article, Facebook, Twitter
import datetime

def statistiques(request):
    
    ###################
    # ARTICLE CLASS
    ###################
    
    site_infos = {}
    date = datetime.datetime.now() - datetime.timedelta(15)
    articles = Article.objects.filter(date__gt=date).all()
    
    for article in articles:
        if site_infos.has_key(article.origine):
            site_infos[article.origine][2] += article.visites
            site_infos[article.origine][3] += 1
        else:
            site_infos[article.origine] = [article.origine, article.lien, article.visites, 1]
    
    tabs_class = [site_infos[key] for key in site_infos.keys()]
    tabs_class.sort(key=lambda x: x[2])
    tabs_class.reverse()
    
    for tab in tabs_class:
        tab.append(tab[2] / tab[3])
        
    ###################
    # FACEBOOK CLASS
    ###################
        
    fb_infos = {}
    date = datetime.datetime.now() - datetime.timedelta(15)
    facebooks = Facebook.objects.filter(date__gt=date).all()
    
    for facebook in facebooks:
        if fb_infos.has_key(facebook.origine):
            fb_infos[facebook.origine][2] += facebook.visites
            fb_infos[facebook.origine][3] += 1
        else:
            fb_infos[facebook.origine] = [facebook.origine, facebook.lien, facebook.visites, 1]
    
    tabs_class_fb = [fb_infos[key] for key in fb_infos.keys()]
    tabs_class_fb.sort(key=lambda x: x[2])
    tabs_class_fb.reverse()
    
    for tab in tabs_class_fb:
        tab.append(tab[2] / tab[3])
        
    ###################
    # TWEET CLASS
    ###################
    
    tw_infos = {}
    date = datetime.datetime.now() - datetime.timedelta(30)
    tweets = Twitter.objects.filter(date__gt=date).all()
    print tweets
    for tweet in tweets:
        if tw_infos.has_key(tweet.origine):
            tw_infos[tweet.origine][1] += tweet.visites
            tw_infos[tweet.origine][2] += 1
        else:
            tw_infos[tweet.origine] = [tweet.origine, tweet.visites, 1]
    
    tabs_class_tw = [tw_infos[key] for key in tw_infos.keys()]
    tabs_class_tw.sort(key=lambda x: x[1])
    tabs_class_tw.reverse()
    
    for tab in tabs_class_tw:
        tab.append(tab[1] / tab[2])
        
    tabs_class_tw = reversed(tabs_class_tw)
            
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'statistiques.html', locals())