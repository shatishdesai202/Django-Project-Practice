from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

def index(request):
    sn = cache.get('surname', 'None')
    if sn == "None":
        sn = cache.set('surname', 'desai', 50)

    return render(request, 'index.html', {'sn':sn})

# def index(request):
#     sn = cache.get_or_set('fees', 4000, 10)
#     cache.get_or_set('fees', 56232, 10, version=2561)
#     # sn=None
#     return render(request, 'index.html', {'surname':sn})


# def index(request):
#     data = {'name':'shatish', 'surname':'desai', 'age':20}
#     cache.set_many(data, 75)
#     sn = cache.get_many(data)
#     # sn=None
#     return render(request, 'index.html', {'sn':sn})

# def index(request):
#     cache.delete('fees', version=2561)
#     return render(request, 'index.html')

# def index(request):
    # # cache.set('fees', 5000 , 60*60*60)
    # sn = cache.get('fees')
    # cache.incr('fees', delta=5)
    # cache.decr('fees', delta=10)
    # return render(request, 'index.html', {'sn':sn})

# def index(request):
#     cache.clear()
#     return render(request, 'index.html')