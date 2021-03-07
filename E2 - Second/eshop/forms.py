from authenticationmodel.forms import CustomSignupForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordChangeForm,UserChangeForm
from .models import Placeorder, Comment

class Placeorder(CustomSignupForm):
    password1 = None
    password2 = None
    username = forms.CharField(label="Username",disabled=True, label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    Add = forms.CharField(label="Address", required=True, label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label="city", required=True, label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label="state", required=True,label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    pin = forms.IntegerField(label="pincode",required=True, label_suffix=" ",
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    
class commentForm(forms.ModelForm):  
    class Meta:
        model = Comment
        fields = (('comment'),)
        widgets={
                   "comment":forms.Textarea(attrs={'placeholder':'Enter Comment','name':'Name','id':'common_id_for_imputfields','class':'form-control','rows':'3'})
                }