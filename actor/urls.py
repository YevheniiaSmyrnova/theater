"""
Actor urls modal
"""
from django.conf.urls import url
from actor import views


urlpatterns = [
    url(r'^$', views.ActorListCreateView.as_view(), name='actor_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor_detail')
]
