from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student
# Create your views here.


class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = "userdetail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_user"] = Student.objects.all().order_by('name') 
        return context

        

class StudentListView(ListView):
    model = Student