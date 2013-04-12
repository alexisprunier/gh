#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article

def accueil(request, page_number):
    
    # recuperation des articles
    all_articles = Article.objects.all().order_by("id")
    size = Article.objects.all().count()
    
    # recuperation des pages
    page_list = []
    i = 1
    while i <= (size-1)/30+1 :
        page_list.append(i)
        i += 1
    
    # selection des article de la page
    selected_article = []
    page_number = int(page_number.encode('ascii'))
    for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
        if ( 0 <= size-(page_number*30-30+i) < size):
            selected_article.append(all_articles[size-(page_number*30-30+i)])
        
    return render(request, 'accueil.html', locals())

def facebook(request):
    
    return render(request, 'facebook.html', locals())

def twitter(request):
    
    return render(request, 'twitter.html', locals())