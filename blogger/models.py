from django.db import models

class User(models.Model):
    username=models.CharField(max_length=200, unique=True)
    usermail=models.EmailField()
    userpassword=models.CharField(max_length=50)
    created_date=models.DateTimeField('Account Created')
    def __str__(self):
        return self.username




class Topic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    topicname=models.CharField(max_length=200, unique=True)
    text=models.TextField()
    pub_date=models.DateTimeField('Date published')
    
    def __str__(self):
        return self.topicname
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    comtext=models.CharField(max_length=200)

    com_date=models.DateTimeField('comment date')
    def __str__(self):
        return self.comtext
    
