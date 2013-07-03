from django.conf.urls import patterns, url

from Restaurant import views

urlpatterns= patterns('',
    url(r'^$',views.index,name='index'),
    # ex: /restaurant/hunans/
    url(r'^(?P<restaurant_name>[a-zA-Z0-9 ]+)/$', views.detail, name='detail'),
    url(r'^(?P<restaurant_name>[a-zA-Z0-9 ]+)/order/$', views.order, name='order'),
    url(r'^(?P<restaurant_name>[a-zA-Z0-9 ]+)/checkout/(?P<selected_dish>[a-zA-Z0-9\-\+\=]+)/$',views.checkout, name='checkout'),
)

'''
urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
'''