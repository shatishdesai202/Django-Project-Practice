from django.contrib import admin
from .models import Page, Like
# Register your models here.

@admin.register(Page)
class AdminPage(admin.ModelAdmin):
    list_display = ['user', 'name']

@admin.register(Like)
class AdminLike(admin.ModelAdmin):
    list_display = ['likes', 'user', 'name']