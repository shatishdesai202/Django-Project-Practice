from django.shortcuts import render
from .forms import StudentForms
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Student
from django import forms
# Create your views here.


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'phone', 'age', 'email']
    template_name = 'todo/student_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_student"] = Student.objects.all() 
        return context
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['phone'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['age'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
        return form

class DeletePageView(DeleteView):
    model = Student
    # template_name = 'todo/student_delete_delete.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_pk = self.request.GET['getpk']
        context["student"] = Student.objects.get(pk=get_pk) 
        return context
    

class CreatePageView(CreateView):
    form_class = StudentForms
    template_name = 'todo/student_form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_student"] = Student.objects.all() 
        return context
    