from django.shortcuts import render,HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .forms import ContactForm
# Create your views here.


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'abc.html'
    success_url = '/thankyoupage/'
    initial = {'name': 'shatish',
               'phone': '12345789',
               'message': 'Enter A Message'}

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['phone'])
        print(form.cleaned_data['message'])
        # return HttpResponse('successfuly submitting form')
        return super().form_valid(form)

class Thankyou(TemplateView):
    template_name = 'thankyou.html'
