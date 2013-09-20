#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def news(request, page_number):
    
    page_number = int(page_number.encode('ascii'))
    selected_articles = get_targeted_articles(page_number)
            
    #page_prec = page_number-1 if page_number > 1 else page_number
    #page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'news.html', locals())

@csrf_exempt
def refresh(request):

    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))
    content = ""
    
    for article in selected_articles:
        content += "\
                <a href='" + str(article.lien) + "'>\
                <div id='article'>\
                    <object id='img_art' type='image/jpeg' data='" + str(article.image) + "'>\
                        <object id='img_art2' type='image/jpeg' data='" + str(request.POST.get('static_url', False)) + "image/empty_image.png'></object>\
                    </object>\
                    <div id='info_art'>\
                        <div id='titre_date'>\
                            <div id='titre_art'>" + str(article.titre) + "</div>\
                            <div id='date_art'>" + str(article.date) + "</div>\
                        </div>\
                        <div id='origine_art'><img id='favicon' src='" + str(request.POST.get('static_url', False)) + "favicon/" + str(article.origine) + ".png' align='bottom' alt='" + str(request.POST.get('static_url', False)) + "image/empty_image.png'></img><div id='text_article'>" + str(article.origine) + "</div></div>\
                    </div>\
                </div>\
                </a>"

    return HttpResponse(content)

def get_targeted_articles(page_number):

    all_articles = Article.objects.all().order_by("id")
    selected_articles = []

    for i in range(30):
        if len(all_articles) > page_number*30+i:
            print page_number*30+i
            selected_articles.append(all_articles[page_number*30+i])
    
    return selected_articles