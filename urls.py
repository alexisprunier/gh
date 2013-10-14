from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('GeekHub.controllers',
    url(r'^accueil/', 'Accueil.accueil'),
    url(r'^news/(\d{4})/?$', 'News.news'),
    url(r'^news/refresh/?$', 'News.refresh'),
    url(r'^facebook/(\d{4})/?$', 'Facebook.facebook'),
    url(r'^facebook/refresh/?$', 'Facebook.refresh'),
    url(r'^twitter/(\d{4})/?$', 'Twitter.twitter'),
    url(r'^twitter/refresh/?$', 'Twitter.refresh'),
    url(r'^sources/', 'Sources.sources'),
    url(r'^statistiques/', 'Statistiques.statistiques'),
    url(r'^admin/', include(admin.site.urls)),
)