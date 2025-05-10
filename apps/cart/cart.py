from decimal import Decimal


class SessionCart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price),
            }
        self.save()

    def sub(self,product, quantity=1):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > quantity:
            self.cart[product_id]['quantity']-=quantity
            self.save()
        else:
            self.remove(product)



    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def save(self):
        self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def get_items(self):
        return self.cart

    def items(self):
        return self.cart.items()


    def total_cart_price(self):
        total_price = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total_price

    # def cart_attributes(self):
    #     cart_attr = {}
    #     cart_attr['total_cart_price'] = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    #     cart_attr['originalPrice']  = Decimal(1.30 * float(cart_attr['total_cart_price']) )
    #     cart_attr['savings']  = Decimal(0.46 *float(cart_attr['total_cart_price']) )
    #     cart_attr['tax']  = Decimal(0.53 * float(cart_attr['total_cart_price']) )
    #
    #     return cart_attr

    def cart_attributes(self):
        cart_attr = {}
        total_price = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        cart_attr['total_cart_price'] = total_price.quantize(Decimal('0.01'))
        cart_attr['originalPrice'] = (total_price * Decimal('1.30')).quantize(Decimal('0.01'))
        cart_attr['savings'] = (total_price * Decimal('0.46')).quantize(Decimal('0.01'))
        cart_attr['tax'] = (total_price * Decimal('0.53')).quantize(Decimal('0.01'))

        return cart_attr



