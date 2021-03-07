from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['p_name', 'p_image', 'p_price', 'p_desc', 'p_category']
