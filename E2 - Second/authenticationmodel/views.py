from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import CustomAuthenticationForm, CustomSignupForm, CustomChangePasswordForm


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'authenticationmodel/login.html'
   

class CustomSignup(CreateView):
    form_class = CustomSignupForm
    template_name = 'authenticationmodel/signup.html'
    success_url = '/authentication/login/'
    

class CustomLogout(LogoutView):
    template_name = 'authenticationmodel/login.html'
    redirect_field_name = 'loginpage'
    

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomChangePasswordForm
    template_name = 'authenticationmodel/passwordchangeform.html'
    success_url = '/profile/'
