from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Student
from .forms import StudentForm
from django import forms
# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     fields = '__all__'
#     # success_url = '/studentdetailview/'
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
#         form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
#         form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
#         return form

class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'cv/student_form.html'


class StudentDetailView(DetailView):
    model = Student

class ThankyouPageView(TemplateView):
    template_name = 'cv/thankyou.html'