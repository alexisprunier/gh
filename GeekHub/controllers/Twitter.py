#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Twitter
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from GeekHub.controllers.Proxy import Proxy

def twitter(request, page_number):
    
    page_number = int(page_number.encode('ascii'))
    selected_articles = get_targeted_articles(page_number)
            
    page_prec = page_number-1 if page_number > 0 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'twitter.html', locals())


@csrf_exempt
def refresh(request):
    
    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))
    content = ""
    
    for article in selected_articles:
        content += "\
                  <a href='https://twitter.com/"+ article.origine +"' target='_blank'><div id='publication_tw'>\
                    <div id='tw_origine'>"+ article.origine +"</div>\
                    <div id='tw_contenu'>"+ article.titre +"</div>\
                    <div id='tw_date'>"+ str(article.date.strftime("%H:%M %d-%m-%Y")) +"</div>\
                  </div></a>"

    return HttpResponse(content)


def get_targeted_articles(page_number):

    all_articles = Twitter.objects.all().order_by("id")
    selected_articles = []

    for i in range(20):
        if len(all_articles) > page_number*20+i:
            selected_articles.append(all_articles[page_number*20+i])
    
    return selected_articles