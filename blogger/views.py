from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    txt="<h1> Welcome to home page </h1> <br><main>Content will be added soon!</main>"
    return HttpResponse(txt)
