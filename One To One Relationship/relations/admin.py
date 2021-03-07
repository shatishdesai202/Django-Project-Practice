from django.contrib import admin
from .models import Informations
# Register your models here.

@admin.register(Informations)
class AdminInformation(admin.ModelAdmin):
    list_display = ['user', 'info']
