from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1', 'password2']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['publisher', 'category']


class NewsCreationForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
