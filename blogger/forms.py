from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Topic

class CommentForm(forms.Form):
    com_name = forms.CharField(label='Your name', max_length=100)
    com_text=forms.CharField(label='Your Comment', max_length=200)
    

class makepostform(forms.Form):
   name=forms.CharField(label='Name of Post', max_length=100)
   txt=forms.CharField(max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your Post!')