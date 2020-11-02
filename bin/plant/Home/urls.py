from django.conf.urls import url
from Home import views

app_name = 'Home'
urlpatterns = [
    url(r'^search/$', views.SearchView, name = 'SearchView'),
    url(r'^search/(?P<name_id>[0-9]+)$', views.ResultView, name = 'ResultView'),
]