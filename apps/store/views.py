from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.template.loader import render_to_string

from apps.products.models import Product, Category
from apps.products.service import ProductService


# def home(request):
#
#     # products = Product.objects.all()  # Fetch all products from the database
#
#     search_query = request.GET.get('search', '')
#
#     items = ProductService.search_items(search_query=search_query)
#
#     context = {
#         'products': items,
#         'search_query': search_query,
#     }
#
#     return render(request, "store/home.html", context)


# def home(request):
#     search_query = request.GET.get('search', '')
#     sort_by = request.GET.get('sortBy', 'title')
#     direction = request.GET.get('direction', 'asc')
#     categories = request.GET.getlist('categories', [])
#
#     items = ProductService.search_products(
#         search_query=search_query,
#         sort_by=sort_by,
#         sort_direction=direction,
#         categories=categories
#     )
#
#     context = {
#         'products': items,
#         'search_query': search_query,
#         'categories': Category.objects.all()
#     }
#
#     return render(request, "store/home.html", context)


def home(request):
    search_query = request.GET.get('title', '')  # Match JS param name
    sort_by = request.GET.get('sortBy', 'title')
    direction = request.GET.get('direction', 'asc')
    categories = request.GET.getlist('categories', [])
    page = int(request.GET.get('page', 0))
    size = int(request.GET.get('size', 20))

    items = ProductService.search_products(
        search_query=search_query,
        sort_by=sort_by,
        sort_direction=direction,
        categories=categories,
        page=page,
        size=size
    )

    context = {
        'products': items,
    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        # This is an AJAX request → return partial template
        html = render_to_string("products_grid.html", context, request=request)
        return HttpResponse(html)

    # Otherwise, render full page
    context['search_query'] = search_query
    context['categories'] = Category.objects.all()
    return render(request, "store/home.html", context)

