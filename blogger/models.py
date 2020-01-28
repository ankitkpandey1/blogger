from django.db import models

class Topic(models.Model):
    topicname=models.CharField(max_length=200, unique=True)
    text=models.TextField()
    pub_date=models.DateTimeField('Date published')

class Comments(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    comtext=models.CharField(max_length=200)
    com_date=models.DateTimeField('comment date')
    
