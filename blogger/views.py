from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Comments
from django.template import loader

def home(request):
    latest=Topic.objects.order_by('-pub_date')[:5]
    output=",".join([q.topicname for q in latest])
    template=loader.get_template('blogger/home.html')
    
    context={
        'latest':latest,
    }
    txt="<h1> Welcome to home page </h1> <br><main>Content will be added soon!</main>"
    return HttpResponse(template.render(context,request))


def details(request, topic_id):
   full=Topic.objects.get(pk=topic_id)
   full.comments_set.all()
   context={'full':full,}
   return render(request,'blogger/details.html',context)