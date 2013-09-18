#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Facebook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def facebook(request, page_number):
    
    page_number = int(page_number.encode('ascii'))
    selected_articles = get_targeted_articles(page_number)
            
    page_prec = page_number-1 if page_number > 1 else page_number
    page_suiv = page_number+1 if page_number < 9 else page_number
    
    return render(request, 'facebook.html', locals())


@csrf_exempt
def refresh(request):
    
    selected_articles = get_targeted_articles(int(request.POST.get('page', False)))
    content = ""
    
    for article in selected_articles:
        content += "\
              <div id='publication'>\
                <div id='fb_origine'>" + article.origine + "</div>\
                <div id='fb_contenu'>" + article.contenu + "</div>\
                <div id='fb_date'>" + str(article.date) + "</div>\
              </div>"

    return HttpResponse(content)


def get_targeted_articles(page_number):

    all_articles = Facebook.objects.all().order_by("id")
    selected_articles = []
    page_number -= 1

    for i in range(10):
        selected_articles.append(all_articles[page_number*10+i])
    
    return selected_articles