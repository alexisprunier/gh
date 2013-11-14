#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article
from GeekHub.controllers.Proxy import Proxy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime


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
    content = ""
    
    for article in selected_articles:
        content += "\
                <a href='" + unicode(article.lien) + "' target='_blank' onclick='add_visite("+ unicode(article.id) +")'>\
                <div id='article'>\
                    <object id='img_art' type='image/jpeg' data='" + unicode(article.image) + "'>\
                        <object id='img_art2' type='image/jpeg' data='" + unicode(request.POST.get('static_url', False)) + "image/empty_image.png'></object>\
                    </object>\
                    <div id='info_art'>\
                        <div id='titre_date'>\
                            <div id='titre_art'>" + unicode(article.titre) + "</div>\
                            <div id='date_art'>" + unicode(article.date.strftime("%H:%M %d-%m-%Y")) + "</div>\
                        </div>\
                        <div id='origine_art'><img id='favicon' src='" + str(request.POST.get('static_url', False)) + unicode(article.origine) + ".png' align='bottom' alt='" + unicode(request.POST.get('static_url', False)) + "image/empty_image.png'></img><div id='text_article'>" + unicode(article.origine) + "</div></div>\
                        <div id='visites_art'>" + unicode(article.visites) + "</div>\
                    </div>\
                </div>\
                </a>"

    return HttpResponse(content)

def get_targeted_articles(page_number):

    all_articles = Article.objects.all().order_by("id")
    all_articles = all_articles.reverse()
    selected_articles = []

    for i in range(24):
        if len(all_articles) > page_number*24+i:
            selected_articles.append(all_articles[page_number*24+i])
    
    return selected_articles

@csrf_exempt
def add_visite(request):

    article = Article.objects.get(id=(int(request.POST.get('id', False))))
    article.visites += 1
    article.save()
    
    
    
    