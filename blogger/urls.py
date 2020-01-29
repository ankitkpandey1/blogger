from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:topic_id>/',views.details, name="Topic details"),
    path('<int:topic_id>/commentform.html',views.comm, name="comments")
        
]