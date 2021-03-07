from django.shortcuts import render

# Create your views here.


def index(request):
    c = request.session.get('count',0)
    count = request.session['count'] = c +1
    
    return render(request, 'index.html',{'c':count})