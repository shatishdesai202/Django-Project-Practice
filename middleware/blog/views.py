from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def index(request):
    print(' i am view')
    return HttpResponse('index page')

def temp(request):
    print('i am template')
    context = {'name':'shatish'}
    return TemplateResponse(request,'index.html' ,context)