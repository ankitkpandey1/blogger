from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Comments
from django.template import loader
from django.urls import reverse
from django.utils import timezone

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
   if request.method == "POST":
       comt=request.POST.get("comtext",None)
       q=full.comments_set.create(comtext=comt,com_date=timezone.now())
       q.save()
       full.comments_set.all()
       context={'full':full,}   
       render(request,'blogger/details.html',context)
   return render(request,'blogger/details.html',context)

