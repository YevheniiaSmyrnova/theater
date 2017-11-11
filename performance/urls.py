"""
Performance urls modal
"""
from django.conf.urls import url
from performance import views


urlpatterns = [
    url(r'^$', views.PerformanceListCreateView.as_view(), name='performance_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.PerformanceRetrieveUpdateDestroyAPIView.as_view(), name='performance_detail')
]