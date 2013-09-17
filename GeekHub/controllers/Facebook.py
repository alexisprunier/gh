#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Facebook
from django.http import HttpResponse

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
    for i in range(10):
        if ( 0 <= size-(page_number*10-10+i) < size):
            selected_article.append(all_articles[size-(page_number*10-10+i)])
            
    # recuperation page suivante et precedente
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'facebook.html', locals())

def refresh(request):

    #return response or better...
    return HttpResponse('ouio')