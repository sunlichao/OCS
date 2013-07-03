from django.conf.urls import patterns, include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'OCS.views.index', name='index'),
    # url(r'^OCS/', include('OCS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    #Project URLS

    #HomePage\

    #Restaurant App
    url(r'^restaurant/', include('Restaurant.urls',namespace='Restaurant')),
)
