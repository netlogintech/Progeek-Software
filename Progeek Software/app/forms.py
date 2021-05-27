from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms
from .models import *
from django import forms

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name","last_name", "email","password1","password2")
        widgets={
        'last_name': forms.TextInput(attrs={'class': 'last_name'}),
        'password':  forms.PasswordInput(attrs={'class': 'password'}),

   		 }
