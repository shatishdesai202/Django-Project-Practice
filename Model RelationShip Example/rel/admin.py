from django.contrib import admin
from .models import Page, Post, Song

# Register your models here.

@admin.register(Page)
class AdminPage(admin.ModelAdmin):
    list_display = ['page_name', 'page_description', 'page_views', 'user']
    

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['post_title', 'post_slug', 'user']

@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'get_user']