# from django.contrib.auth import login
from django.urls import path
from .views import home
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home', permanent=False)),
    path("home/", home, name='home'),
    path("home/search-view", home, name='home_search_view')



]