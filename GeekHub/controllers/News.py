#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article


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
    for i in range(30):
        if ( 0 <= size-(page_number*10-10+i) < size):
            selected_article.append(all_articles[size-(page_number*10-10+i)])
            
    # recuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'news.html', locals())