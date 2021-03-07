from django.shortcuts import render
from .models import Page, Post, Song
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_(request):

    data = User.objects.all()
    data1 = User.objects.filter(page__page_name="harshil page")
    data2 = User.objects.filter(page__page_views=10)
    data3 = User.objects.filter(
        page__page_description="Dharmik page description")
    # print(data2.query)
    # POST TABLE
    data4 = User.objects.filter(post__user__username__icontains="desai")
    data5 = User.objects.filter(post__post_title="CA foundation post")
    # SONG

    data6 = User.objects.filter(song__song_duration=12)
    data7 = User.objects.filter(song__user__username__icontains="jeel")
    data8 = User.objects.filter(song__song_name="malang malang")

    context = {'data': data, 'data1': data1, 'data2': data2,
               'data3': data3, 'data4': data4, "data5": data5, 'data6': data6, 'data7': data7, 'data8': data8}

    return render(request, 'user.html', context)


def page_(request):
    data = Page.objects.all()
    data1 = Page.objects.filter(page_name='shatish page')
    data2 = Page.objects.filter(page_views=10)
    data3 = Page.objects.filter(user__username__icontains="desai")
    context = {'data': data, 'data1': data1, 'data2': data2, 'data3':data3}
    return render(request, 'page.html', context)


def post_(request):
    data = Post.objects.all()
    data1 = Post.objects.filter(post_slug='Ca foundation')
    context = {'data':data, 'data1':data1}
    return render(request, 'post.html', context)


def song_(request):

    data = Song.objects.all()
    data1 = Song.objects.filter(song_duration=12)
    data2 = Song.objects.filter(user__username='desai')
    context ={'data':data, 'data1':data1, 'data2':data2}
    return render(request, 'song.html', context)
