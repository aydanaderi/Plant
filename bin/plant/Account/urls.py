from django.conf.urls import url
from Account import views

app_name = 'signup'
urlpatterns = [
    url(r'^signup/$', views.SignupView, name = 'SignupView'),
    url(r'^login/$', views.LoginView, name = 'LoginView'),
    url(r'^profile/$', views.ProfileView, name = 'HomeView'),
    url(r'^user/$', views.UserView, name = 'UserView'),
    url(r'basic/$', views.BasicView, name = 'BasicView'),
    url(r'upload/$', views.UploadView, name = 'UploadView'),
    url(r'logout/$', views.LogoutView, name = 'LogoutView'),
    url(r'change_password/$', views.Change_passwordView, name = 'Change_passwordView'),
]