from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('GeekHub.controllers',
    url(r'^accueil/', 'Accueil.accueil'),
    url(r'^refresh_nw/?$', 'Accueil.refresh_nw'),
    url(r'^refresh_fb/?$', 'Accueil.refresh_fb'),
    url(r'^refresh_tw/?$', 'Accueil.refresh_tw'),
    url(r'^news/(\d{1})/?$', 'News.news'),
    url(r'^news/refresh/?$', 'News.refresh'),
    url(r'^news/add_visite/?$', 'News.add_visite'),
    url(r'^facebook/(\d{1})/?$', 'Facebook.facebook'),
    url(r'^facebook/refresh/?$', 'Facebook.refresh'),
    url(r'^twitter/(\d{1})/?$', 'Twitter.twitter'),
    url(r'^twitter/refresh/?$', 'Twitter.refresh'),
    url(r'^sources/', 'Sources.sources'),
    url(r'^statistiques/', 'Statistiques.statistiques'),
    url(r'^admin/', include(admin.site.urls)),
)