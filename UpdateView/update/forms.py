from django import forms
from .models import Student

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),
        'phone': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
        'password': forms.TextInput(attrs={'class':'form-control'}),}