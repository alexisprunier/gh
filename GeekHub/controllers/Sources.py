#-*- coding: utf-8 -*-
from django.shortcuts import render

def sources(request):
    
    return render(request, 'sources.html', locals())