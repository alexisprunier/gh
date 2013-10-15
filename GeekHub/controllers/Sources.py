#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.controllers.Proxy import Proxy


def sources(request):
    
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'sources.html', locals())