from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_view

from .forms import CustomAuthenticationForm, CustomePasswordChangeForm

urlpatterns = [
    path('',  TemplateView.as_view(
        template_name="authentication/home.html"), name="home"),

    path('login/',  auth_view.LoginView.as_view(
        template_name="authentication/login.html", form_class=CustomAuthenticationForm), name="loginpage"),

    path('dashboard/',  TemplateView.as_view(
        template_name="authentication/dashboard.html"), name="dashboardpage"),

    path('logout/',  auth_view.LogoutView.as_view(
        template_name="authentication/logout.html"), name="logout"),
    
    path('changepasswordpage/',  auth_view.PasswordChangeView.as_view(
        template_name="authentication/changepassword.html",  form_class=CustomePasswordChangeForm, success_url="/passwordchangedone/"), name="changepasswordpage"),
    
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name="authentication/changepassworddone.html"), name="passwordchangedone"),
 
]
