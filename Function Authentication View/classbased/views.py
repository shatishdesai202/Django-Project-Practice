from django.shortcuts import render
from django.views.generic.base import TemplateView
from  django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


@method_decorator(login_required, name="dispatch")
class ProfilePage(TemplateView):
    template_name = 'profile.html'

@method_decorator(staff_member_required, name="dispatch")
class AboutPage(TemplateView):
    template_name = 'about.html'
