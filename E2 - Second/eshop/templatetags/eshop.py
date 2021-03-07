from django import template
from eshop.models import Category

register = template.Library()


@register.filter(name="cat_count")
def cat_count(id):
    return Category.objects.filter(product__category=id).count()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name="item_count")
def item_count(product, cart):
    keys = cart.keys()

    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False




@register.filter(name="item_total")
def item_total(product, cart):
    return product.price * item_count(product, cart)
    

@register.filter(name="total_bill")
def total_bill(product, cart):
    sum = 0
    for p in product:
        sum = sum + item_total(p, cart)
    return sum

