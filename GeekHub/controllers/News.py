#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article
from GeekHub.controllers.Proxy import Proxy
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from settings import STATIC_URL


def news(request, page_number):
    
    page_number = int(page_number.encode('ascii'))
    selected_articles = get_targeted_articles(page_number)
            
    page_prec = page_number-1 if page_number > 0 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    
    
    return render(request, 'news.html', locals())

@csrf_exempt
def refresh(request):

    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))
    
    html = render_to_string('ajax_template/ajax_news.html', {'selected_articles':selected_articles, 'STATIC_URL':STATIC_URL, "ajax":True})
    return HttpResponse(html)

def get_targeted_articles(page_number):
    nb_news = 30
    all_articles = Article.objects.all().order_by("date")[nb_news*page_number:nb_news*(page_number+1)]
    all_articles = all_articles.reverse()

    
    
    return all_articles

@csrf_exempt
def add_visite(request):

    article = Article.objects.get(id=(int(request.POST.get('id', False))))
    article.visites += 1
    article.save()
    
@csrf_exempt
def get_articles(request):
    keyword = str(request.POST["text"])
    articles = Article.objects.filter(titre__icontains = keyword ).order_by("date")
    html = render_to_string('ajax_template/ajax_news.html', {'selected_articles':articles, 'STATIC_URL':STATIC_URL, "ajax":True})
    return HttpResponse(html)
    
    
    
    