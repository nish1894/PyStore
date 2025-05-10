# from django.contrib.auth import login
from django.urls import path
from .views import register, signin, home,logout_view, profile


urlpatterns = [

    path("register/",register,name='register'),
    path("login/", signin, name = 'login'),
    path("home/", home, name ='home'),
    path("profile/",profile, name = 'profile'),
    path("logout/", logout_view, name='logout'),

]