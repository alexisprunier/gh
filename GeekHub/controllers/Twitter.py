#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Twitter
from GeekHub.controllers.Proxy import Proxy


def twitter(request, page_number):
    
    # recuperation des articles
    all_articles = Twitter.objects.all().order_by("id")
    size = Twitter.objects.all().count()
    
    # recuperation des pages
    page_list = []
    i = 1
    while i <= (size-1)/20+1 :
        page_list.append(i)
        i += 1
    
    # selection des article de la page
    selected_article = []
    page_number = int(page_number.encode('ascii'))
    for i in range(20):
        if ( 0 <= size-(page_number*20-20+i) < size):
            selected_article.append(all_articles[size-(page_number*10-10+i)])
            
    # récuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'twitter.html', locals())