"""
Schedule urls modal
"""
from django.conf.urls import url
from schedule import views


urlpatterns = [
    url(r'^$', views.ScheduleListCreateView.as_view(), name='schedule_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.ScheduleRetrieveUpdateDestroyAPIView.as_view(), name='schedule_detail')
]
