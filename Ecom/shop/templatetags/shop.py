from django import template
from shop.models import Category


register = template.Library()

@register.filter(name="category_count")
def category_count(id):
    return Category.objects.filter(product__p_category=id).count()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
            # return "it's ok"
    return False

@register.filter(name="item_count")
def item_count(product, cart):
    keys = cart.keys()

    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
            # return "it's ok"
    return False