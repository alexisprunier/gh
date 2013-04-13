from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('GeekHub.views',
    url(r'^', 'accueil'),
    url(r'^web/(\d{4})/?$', 'web'),
    url(r'^facebook/', 'facebook'),
    url(r'^admin/', include(admin.site.urls)),
)