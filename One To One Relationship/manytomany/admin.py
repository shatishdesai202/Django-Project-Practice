from django.contrib import admin
from .models import Song
# Register your models here.


@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    
    list_display = ['name', 'length', 'all_singer']