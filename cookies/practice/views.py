from django.shortcuts import render

# Create your views here.


def setcookies(request):
    c = request.session.get('count', 0)
    counter = c+1
    request.session['count'] = counter

    tst = request.session['count']
    request.session['name'] = 'shatish'
    request.session['sirname'] = 'desai'
    request.session['framework'] = 'Django'
    keys = request.session.items()
    return render(request, 'setcookies.html', {'tst':tst, 'key':keys})

def getcokkies(request):
    if 'count' in request.session:
        tst= request.session['count']
    else:
        tst = 'no cookies'
    return render(request, 'getcookies.html', {'tst':tst})


def delcookies(request):
    request.session.clear_expired()
    request.session.flush()
    return render(request, 'delcookies.html',)