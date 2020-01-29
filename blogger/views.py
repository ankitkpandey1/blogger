from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Comments,  User
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .forms import CommentForm,makepostform,userform,loginform
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
            usd=request.session['id']
            x=User.objects.get(pk=usd)
            q=full.comments_set.create(comtext=comt,com_date=timezone.now(),user=x)
            q.save()
            context={'full':full,}  
            tx='/blogger/'+str(topic_id)
            return redirect(tx) 
    else:
        form=CommentForm()
    return render(request,'blogger/commentform.html',{'form':form})
def makepost(request):
    form1=makepostform()
    if request.method == "POST":
        form1=makepostform(request.POST)
        if form1.is_valid():
            try:
                tname=form1.cleaned_data["name"]
                tx=form1.cleaned_data["txt"]
                usd=request.session['id']
                x=User.objects.get(pk=usd)
                q = Topic(topicname=tname,text=tx, pub_date=timezone.now(),user=x)
                q.save()
                return redirect('/blogger/')
            except Exception as e:
                return HttpResponse("Fatal error ")
    else:
        form1=makepostform()
    return render(request,'blogger/makepost.html',{'form1':form1})

def userreg(request):
    form1=userform()
    if request.method == "POST":
        form1=userform(request.POST)
        if form1.is_valid():
            try:
                usernam=form1.cleaned_data['username']
                userpass=form1.cleaned_data['password']
                usermai=form1.cleaned_data['usermail']
                q= User(username=usernam,userpassword=userpass,usermail=usermai,created_date=timezone.now())
                q.save()
                reuqest.session['id']=q.id
                return redirect('/blogger')
            except Exception as e:
                return HttpResponse("Fatal Error")
    else:
        form1=userform()
    return render(request,'blogger/userregister.html',{'form1':form1})

def login(request):
    form2=loginform()
    if request.method == "POST":
        form2=loginform(request.POST)
        if form2.is_valid():
            try:
                usnam=form2.cleaned_data['user_name']
                uspass=form2.cleaned_data['user_password']
                q=User.objects.get(username=usnam,userpassword=uspass)
                request.session['id']=q.id
                return HttpResponse("<h1>Login successful</h1>")
            except: 
                return HttpResponse("<h1>Invalid details</h1>")
        
    else:
        form2=loginform()
    return render(request,'blogger/login.html',{ 'form2' : form2 })
    
        