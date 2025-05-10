from django.urls import path
from .views import api_add_to_cart, home, cart

app_name = 'cart'

urlpatterns = [
    path('api/update/', api_add_to_cart, name='api_update_cart'),
    path("home/", home, name='home'),
    path ('', cart, name='cart')
]
