from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class LoginForm(forms.Form):
    username= forms.CharField(max_length=100,label='username')
    password = forms.CharField(max_length=100,label='password',widget=forms.PasswordInput)




