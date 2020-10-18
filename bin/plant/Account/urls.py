from django.conf.urls import url
from Account import views

app_name = 'signup'
urlpatterns = [
    url(r'^signup/$', views.SignupView, name = 'SignupView'),
    url(r'^login/$', views.LoginView, name = 'LoginView'),
    url(r'^profile/$', views.ProfileView, name = 'HomeView'),
    url(r'^user/$', views.UserView, name = 'UserView'),
    url(r'basic/$', views.BasicView, name = 'BasicView'),
    url(r'uploadprofile/$', views.UploadprofileView, name = 'UploadprofileView'),
    url(r'logout/$', views.LogoutView, name = 'LogoutView'),
    url(r'change_password/$', views.Change_passwordView, name = 'Change_passwordView'),
    url(r'checkemail/$', views.Check_emailView, name = 'Check_email'),
    url(r'resetpasssword/$', views.Reset_passwordView, name = 'Reset_password'),
]