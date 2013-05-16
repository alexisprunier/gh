from django.db import models
from django.contrib import admin

class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    origine = models.CharField(max_length=42)
    lien = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    image = models.CharField(max_length=200)
    vote_pos = models.IntegerField(null=True)
    vote_neg = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.titre
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'origine', 'lien', 'date', 'image')
    search_fields = ('id', 'titre', 'origine', 'lien', 'date', 'image')

class Facebook(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    origine = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    lien = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    
    def __unicode__(self):
        return self.titre
    
class FacebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')
    search_fields = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')
    
class Twitter(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    origine = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    lien = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    
    def __unicode__(self):
        return self.titre
    
class TwitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')
    search_fields = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')

admin.site.register(Facebook, FacebookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Twitter, TwitterAdmin)