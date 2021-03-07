from django.contrib import admin
from .models import Info
# Register your models here.


@admin.register(Info)
class AdminInfo(admin.ModelAdmin):
    list_display = ['name']