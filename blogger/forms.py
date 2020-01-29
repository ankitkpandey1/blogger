from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Topic, User

class CommentForm(forms.Form):
   
    com_text=forms.CharField(label='Your Comment', max_length=200)
    

class makepostform(forms.Form):
   name=forms.CharField(label='Name of Post', max_length=100)
   txt=forms.CharField(max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your Post!')
class userform(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username', 'usermail']
        
        
class loginform(forms.Form):
    user_name=forms.CharField(max_length=200)
    user_password=forms.CharField(max_length=50)