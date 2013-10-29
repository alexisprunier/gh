#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article, Facebook, Twitter
from GeekHub.controllers.Proxy import Proxy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def accueil(request):
    
    last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-4:])
    last_articles = reversed(last_articles)
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]
    last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]
    
    proxy = Proxy()
    best_article = proxy.get_most_visited_article()
    best_site = proxy.get_most_visited_site()
    
    return render(request, 'accueil.html', locals())

@csrf_exempt
def refresh_nw(request):
    
    last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-4:])
    last_articles = reversed(last_articles)

    content = ""
    
    for article in last_articles:
        content += "\
                <a href='" + unicode(article.lien) + "' target='_blank'>\
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

@csrf_exempt
def refresh_tw(request):
    
    last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]

    content = ""
    
    for article in last_twitter:
        content += "\
                  <a href='https://twitter.com/"+ article.origine +"' target='_blank'><div id='publication_tw'>\
                    <div id='tw_origine'>"+ article.origine +"</div>\
                    <div id='tw_contenu'>"+ article.titre +"</div>\
                    <div id='tw_date'>"+ str(article.date.strftime("%H:%M %d-%m-%Y")) +"</div>\
                  </div></a>"

    return HttpResponse(content)

@csrf_exempt
def refresh_fb(request):
    
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]
         
    content = ""
    
    for article in last_facebook:
        content += "\
            <a href='' target='_blank'>\
              <div id='publication' target='_blank'>\
                <div id='fb_origine'>" + article.origine + "</div>\
                <div id='fb_contenu'>" + article.contenu + "</div>\
                <div id='fb_date'>" + str(article.date.strftime("%H:%M %d-%m-%Y")) + "</div>\
                <div id='fb_visites'>" + unicode(article.visites) + "</div>\
              </div>\
            </a>"

    return HttpResponse(content)