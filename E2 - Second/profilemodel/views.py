from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import update_session_auth_hash
from .forms import CustomSignupForm
# Create your views here.


class ChangeProfile(View):
    
    def get(self, request):
        form = CustomSignupForm(instance=request.user)
        context = {'form': form}
        return render(request, 'profilemodel/profile.html', context)
    
    