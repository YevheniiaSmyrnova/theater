"""
News urls modal
"""
from django.conf.urls import url
from news import views


urlpatterns = [
    url(r'^$', views.NewsListCreateView.as_view(), name='news_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.NewsRetrieveUpdateDestroyAPIView.as_view(), name='news_detail')
]
