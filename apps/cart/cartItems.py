from apps.products.models import Product


class CartItem:
    def __init__(self, product, quantity):
        self.itemId = product.id
        self.title = product.title
        self.price = product.price
        self.itemImage = product.image if product.image else None
        self.quantity = quantity
        self.totalPrice = quantity * product.price

def build_cart(session_cart):
    cart_items = []
    for product_id, item_data in session_cart.items():
        try:
            product = Product.objects.get(id=product_id)
            quantity = item_data['quantity']
            cart_items.append(CartItem(product, quantity))
        except Product.DoesNotExist:
            # Optionally handle missing products
            continue
    return cart_items