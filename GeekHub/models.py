from django.db import models
from django.contrib import admin

class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True, null=True)
    origine = models.CharField(max_length=42)
    lien = models.TextField()
    short_link = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    image = models.CharField(max_length=200, null=True)
    visites = models.IntegerField(null=True, default=0)
    
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
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    visites = models.IntegerField(null=True, default=0)
    
    def __unicode__(self):
        return self.titre
    
class FacebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')
    search_fields = ('id', 'titre', 'origine', 'contenu', 'lien', 'date')
    
class Twitter(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    origine = models.CharField(max_length=42)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    visites = models.IntegerField(null=True, default=0)
    
    def __unicode__(self):
        return self.titre
    
class TwitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'origine', 'date')
    search_fields = ('id', 'titre', 'origine', 'date')

admin.site.register(Facebook, FacebookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Twitter, TwitterAdmin)