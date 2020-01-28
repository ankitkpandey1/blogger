from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

def home(request):
    latest=Topic.objects.order_by('-pub_date')[:5]
    output=",".join([q.topicname for q in latest])
    txt="<h1> Welcome to home page </h1> <br><main>Content will be added soon!</main>"
    return HttpResponse(output)
def details(request, topic_id):
    return HttpResponse("Details")