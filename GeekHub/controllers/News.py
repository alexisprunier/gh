#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article
from GeekHub.controllers.Proxy import Proxy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.template.loader import render_to_string
from settings import STATIC_URL

GLOBAL_nb_news = 24
def news(request, page_number):
    
    day = str(datetime.date.today().day)
    page_number = int(page_number.encode('ascii'))
    selected_articles = get_targeted_articles(page_number)
            
    page_prec = page_number-1 if page_number > 0 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'news.html', locals())

@csrf_exempt
def refresh(request):

    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))    
    html = render_to_string('ajax_content/ajax_news.html', {'selected_articles':selected_articles, 'STATIC_URL':STATIC_URL})
    return HttpResponse(html)
@csrf_exempt
def next_news(request):

    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))    
    html = render_to_string('ajax_content/ajax_news.html', {'selected_articles':selected_articles, 'STATIC_URL':STATIC_URL})
    return HttpResponse(html)
def get_targeted_articles(page_number):

    selected_articles = Article.objects.all()[(page_number)*24:GLOBAL_nb_news + GLOBAL_nb_news * page_number]
   
    return selected_articles

@csrf_exempt
def add_visite(request):

    article = Article.objects.get(id=(int(request.POST.get('id', False))))
    article.visites += 1
    article.save()
    
    
    
    