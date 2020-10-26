from django.conf.urls import url
from Home import views

app_name = 'Home'
urlpatterns = [
    url(r'^home/$', views.HomeView, name = 'HomeView'),
    url(r'^search/$', views.SearchView, name = 'SearchView'),
]