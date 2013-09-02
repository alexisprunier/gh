#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article, Facebook, Twitter

def accueil(request):
    
    last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-4:])
    last_articles = reversed(last_articles)
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]
    last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]
    return render(request, 'accueil.html', locals())

def news(request, page_number):
    
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
            
    # récuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
        
    return render(request, 'news.html', locals())

def facebook(request, page_number):
    
    # recuperation des articles
    all_articles = Facebook.objects.all().order_by("id")
    size = Facebook.objects.all().count()
    
    # recuperation des pages
    page_list = []
    i = 1
    while i <= (size-1)/10+1 :
        page_list.append(i)
        i += 1
    
    # selection des article de la page
    selected_article = []
    page_number = int(page_number.encode('ascii'))
    for i in [1,2,3,4,5,6,7,8,9,10]:
        if ( 0 <= size-(page_number*10-10+i) < size):
            selected_article.append(all_articles[size-(page_number*10-10+i)])
            
    # récuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'facebook.html', locals())

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
    for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
        if ( 0 <= size-(page_number*20-20+i) < size):
            selected_article.append(all_articles[size-(page_number*10-10+i)])
            
    # récuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'twitter.html', locals())

def sources(request):
    
    return render(request, 'sources.html', locals())

def apropos(request):
    
    return render(request, 'apropos.html', locals())