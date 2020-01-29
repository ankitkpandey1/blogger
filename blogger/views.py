from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Comments
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .forms import CommentForm
from django.shortcuts import redirect

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

def comm(request, topic_id):
    full=Topic.objects.get(pk=topic_id)
    full.comments_set.all()
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comt=form.cleaned_data["com_text"]
            q=full.comments_set.create(comtext=comt,com_date=timezone.now())
            q.save()
            context={'full':full,}  
            tx='/blogger/'+str(topic_id)
            return redirect(tx) 
    else:
        form=CommentForm()
    return render(request,'blogger/commentform.html',{'form':form})