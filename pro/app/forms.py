from django.core import validators
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class sing(UserCreationForm):
    first_name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Emial'})

    class Meta:
        
    
               




        model = User
        fields = ('username','first_name', 'email')
        labels = {'email':'Email','first_name':'Name'}
#log

