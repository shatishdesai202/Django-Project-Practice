from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.


def index(request):
    
    post = Post.objects.all()

    paginator = Paginator(post,3)
    
    
    page_number = request.GET.get('page')
    

    page_object = paginator.get_page(page_number)
    
    context = {'page_obj':page_object }

    return render(request, 'pages/index.html', context)