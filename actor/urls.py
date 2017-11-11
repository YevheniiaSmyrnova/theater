from django.conf.urls import url
from actor import views


urlpatterns = [
    url(r'^$', views.ListActorView.as_view(), name='list_create'),
]
