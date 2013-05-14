from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('GeekHub.views',
    url(r'^accueil/', 'accueil'),
    url(r'^news/(\d{4})/?$', 'news'),
    url(r'^facebook/(\d{4})/?$', 'facebook'),
    url(r'^twitter/(\d{4})/?$', 'twitter'),
    url(r'^admin/', include(admin.site.urls)),
)