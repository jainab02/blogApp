from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields= ['blog','photos']

class UserRegistration(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields= ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }