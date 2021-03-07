from django.shortcuts import render

# Create your views here.

def index(request):

    c = request.session.get('count', 0)
    counter =  c+1
    request.session['count'] = counter 


    return render(request, 'index.html', {'count':counter})