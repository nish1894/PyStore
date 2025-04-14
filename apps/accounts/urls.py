# from django.contrib.auth import login
from django.urls import path
from .views import register, login

urlpatterns = [
    path("register/",register),
    path("login/", login)

]