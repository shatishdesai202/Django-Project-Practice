from django.contrib import admin
from .models import Category, Product, Placeorder, Comment
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'c_name']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','category', 'p_name', 'price', 'desc', 'timestamp']


@admin.register(Placeorder)
class AdminPlaceorder(admin.ModelAdmin):
    list_display = ['id','firstname', 'last_name', 'email', 'address', 'city', 'state', 'pin', 'item', 'qty', 'customer', ]

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['comment']