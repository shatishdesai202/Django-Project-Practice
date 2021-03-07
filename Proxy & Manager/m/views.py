from django.shortcuts import render, HttpResponse
from .models import Student, ProxyStudent

# Create your views here.

def index(request):
    # st = Student.objects.all()
    # st = Student.rng.get_abcd(101,103)
    # st = Student.abc.all()
    # st = ProxyStudent.objects.all()
    st = ProxyStudent.reverse.rangerID(101,104)
    print(st)  
    return render(request, 'index.html',{'st':st})
