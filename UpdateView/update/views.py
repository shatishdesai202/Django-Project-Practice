from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from .models import Student
from .forms import StudentForms
# Create your views here.

class CreateViewPage(CreateView):
    # model = Student
    # fields = ['name', 'phone', 'email', 'password']
    form_class = StudentForms
    template_name = 'update/student_form.html'
    # success_url = 'thanks'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_Students"] = Student.objects.all() 
        return context
    
    # def get_form(self):
    #     form =  super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
    #     form.fields['phone'].widget = forms.TextInput(attrs={'class':'form-control'})
    #     form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
    #     return form
    

class UpdateViewPage(UpdateView):
    # model = Student
    # fields = ['name', 'phone', 'email', ]
    # success_url = '/updatethanks/'
    model = Student
    form_class = StudentForms
    template_name = 'update/student_form.html'
    success_url = '/'

    # def get_form(self):
    #     form =  super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
    #     form.fields['phone'].widget = forms.TextInput(attrs={'class':'form-control'})
    #     form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
    #     form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
    #     return form