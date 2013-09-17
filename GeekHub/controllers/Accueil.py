#-*- coding: utf-8 -*-
from django.shortcuts import render
from GeekHub.models import Article, Facebook, Twitter


def accueil(request):
    
    last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-4:])
    last_articles = reversed(last_articles)
    last_facebook = Facebook.objects.all().order_by("id")[Facebook.objects.all().order_by("id").count()-1:]
    last_twitter = Twitter.objects.all().order_by("id")[Twitter.objects.all().order_by("id").count()-3:]
    return render(request, 'accueil.html', locals())