from django.conf.urls import url
from Account import views

app_name = 'Account'
urlpatterns = [
    url(r'^$', views.BasicView, name = 'BasicView'),
    url(r'^signup/$', views.SignupView, name = 'SignupView'),
    url(r'^login/$', views.LoginView, name = 'LoginView'),
    url(r'^profile/$', views.ProfileView, name = 'HomeView'),
    url(r'^user/$', views.UserView, name = 'UserView'),
    url(r'^upload_profile/$', views.UploadـProfileView, name = 'UploadـprofileView'),
    url(r'^logout/$', views.LogoutView, name = 'LogoutView'),
    url(r'^change_password/$', views.Change_passwordView, name = 'Change_passwordView'),
    url(r'^check_email/$', views.Check_emailView, name = 'Check_email'),
    url(r'^(?P<username_id>[0-9]+)/reset/$', views.Reset_passwordView , name = 'Reset_password'),
    url(r'^show_messages/$', views.ShowMessagesView, name = 'ShowMessagesView'),
]