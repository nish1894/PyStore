from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from apps.products.models import Product


def home(request):

    products = Product.objects.all()  # Fetch all products from the database
    return render(request, "store/home.html", {"products": products})