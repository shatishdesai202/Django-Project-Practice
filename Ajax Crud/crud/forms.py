from .models import Detail
from django import forms

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control' , 'id':'nameinput'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'emailinput'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'id':'passwordinput'}),
        }