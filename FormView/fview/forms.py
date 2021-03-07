from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    phone = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.Textarea)