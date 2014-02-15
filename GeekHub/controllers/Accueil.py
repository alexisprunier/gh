#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article, Facebook, Twitter
from GeekHub.controllers.Proxy import Proxy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import render_to_string
from settings import STATIC_URL


def accueil(request):
    
    
    selected_articles = Article.objects.all().order_by("date")[:4].reverse()
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]
    '''last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]
    last_twitter = reversed(last_twitter)'''
    proxy = Proxy()
    #best_article = proxy.get_most_visited_article()
    #best_site = proxy.get_most_visited_site()
    
    return render(request, 'accueil.html', locals())

@csrf_exempt
def refresh_nw(request):
    
    selected_articles = Article.objects.all().order_by("date")[:4].reverse()
    
    html = render_to_string('ajax_template/ajax_news.html', {'selected_articles':selected_articles, 'STATIC_URL':STATIC_URL, "ajax":True})
    return HttpResponse(html)

@csrf_exempt
def refresh_tw(request):
    
    last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]
    last_twitter = reversed(last_twitter)
    
    content = ""
    
    for article in last_twitter:
        content += "\
                  <a href='https://twitter.com/"+ article.origine +"' target='_blank' onclick='add_visite_tw("+ unicode(article.id) +")'><div id='publication_tw'>\
                    <div id='tw_origine'>"+ article.origine +"</div>\
                    <div id='tw_contenu'>"+ article.titre +"</div>\
                    <div id='tw_date'>"+ str(article.date.strftime("%H:%M %d-%m-%Y")) +"</div>\
                    <div id='tw_visites'>"+ unicode(article.visites) +"</div>\
                  </div></a>"

    return HttpResponse(content)

@csrf_exempt
def refresh_fb(request):
    
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]

    content = ""
    
    for article in last_facebook:
        content += "\
            <a href='' target='_blank'>\
              <div id='publication' target='_blank' onclick='add_visite_fb("+ unicode(article.id) +")'>\
                <div id='fb_origine'>" + article.origine + "</div>\
                <div id='fb_contenu'>" + article.contenu + "</div>\
                <div id='fb_date'>" + str(article.date.strftime("%H:%M %d-%m-%Y")) + "</div>\
                <div id='fb_visites'>" + unicode(article.visites) + "</div>\
              </div>\
            </a>"

    return HttpResponse(content)