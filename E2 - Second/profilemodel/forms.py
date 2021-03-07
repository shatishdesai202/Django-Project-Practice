from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User


class CustomSignupForm(UserCreationForm):
    
    password1 = None
    password2 = None
    username = forms.CharField(label="User Name",disabled=True, label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label="First Name",disabled=True, label_suffix=" ",
                                 required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label="Last Name",disabled=True, label_suffix=" ",
                                required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="Email",disabled=True, label_suffix=" ",
                                required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'},),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), }