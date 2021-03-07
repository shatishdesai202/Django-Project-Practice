from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignupForm

# Create your views here.

def sign(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignupForm()

    else:
        form = SignupForm()

    context = {'form':form}
    return render(request, 'base.html', context) 
