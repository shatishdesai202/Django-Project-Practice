from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )


class CustomSignupForm(UserCreationForm):
    password1 = forms.CharField(label='Create Password', label_suffix=" ",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', label_suffix=" ",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label="User Name", label_suffix=" ",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label="First Name", label_suffix=" ",
                                 required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label="Last Name", label_suffix=" ",
                                required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="Email", label_suffix=" ",
                                required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'},),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}), }


class CustomChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Enter OldPassword', label_suffix=" ",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    new_password1 = forms.CharField(label='Create NewPassword', label_suffix=" ",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    new_password2 = forms.CharField(label='Confirm NewPassword', label_suffix=" ",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
