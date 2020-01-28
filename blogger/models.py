from django.db import models

class Topic(models.Model):
    topicname=models.CharField(max_length=200, unique=True)
    text=models.TextField()
    pub_date=models.DateTimeField('Date published')
    def __str__(self):
        return self.topicname
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comments(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    comtext=models.CharField(max_length=200)
    com_date=models.DateTimeField('comment date')
    def __str__(self):
        return self.comtext
    
