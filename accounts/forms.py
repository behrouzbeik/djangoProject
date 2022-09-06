from django import forms
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    password_1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password_2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email exist')
        return email