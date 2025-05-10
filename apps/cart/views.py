from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .cart import SessionCart
from .cartItems import build_cart
from ..products.models import Product


@csrf_exempt  # For quick start; ideally handle CSRF properly
def api_add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('itemId')
        action = data.get('action')
        print("cart post request",product_id,action )

        try:
           product = Product.objects.get(id=product_id)
           cart = SessionCart(request)
           print("Product ID:", product_id, "Action:", action)
           if action == 'add':
                cart.add(product)
           elif action == 'sub':
                cart.sub(product)
           else:
                cart.remove(product)

        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        return JsonResponse({'status': 'ok', 'cart_size': len(cart.cart)})
    return JsonResponse({'error': 'Invalid method'}, status=405)

def home(request):
    # return HttpResponse("This is register page")
    return render(request,"cart/home.html",{})

def cart(request):
    cart = SessionCart(request)
    cart_items = build_cart(cart)

    # cart_Attributes = {}
    # cart_Attributes['total_cart_price'] = cart.total_cart_price()
    cart_attr = cart.cart_attributes()

    for item in cart_items:
        print("cart item:", item.totalPrice)
    return render(request,"cart/cart.html",{"items" : cart_items,'attr' : cart_attr   })



# @csrf_exempt
# def api_add_to_cart(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         item_id = data.get('itemId')  # Match JavaScript parameter name
#         action = data.get('action')
#
#         try:
#             product = Product.objects.get(id=item_id)
#             cart = SessionCart(request)
#
#             if action == 'add':
#                 cart.add(product)
#             elif action == 'sub':
#                 cart.sub(product)
#             elif action == 'remove':
#                 cart.remove(product)
#
#             return JsonResponse({
#                 'status': 'ok',
#                 'itemCount': len(cart.cart),
#                 'items': cart.get_items()
#             })
#
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found'}, status=404)
#
#     return JsonResponse({'error': 'Invalid method'}, status=405)