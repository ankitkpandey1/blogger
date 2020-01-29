from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:topic_id>/',views.details, name="Topic details"),
    path('<int:topic_id>/commentform.html',views.comm, name="comments"),
    path('makepost',views.makepost, name='makepost'),
    path('register',views.userreg, name="register user"),
    path('login',views.login,name="user login")
        
]