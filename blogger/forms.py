from django import forms

class CommentForm(forms.Form):
    com_name = forms.CharField(label='Your name', max_length=100)
    com_text=forms.CharField(label='Your Comment', max_length=200)