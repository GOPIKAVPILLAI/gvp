from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    def __str__(self):
        return self.fname

class fff(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    det =models.CharField(max_length=234,null=True)
    participants=models.ManyToManyField(User,related_name='participant' ,blank=True)
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.det
    

class msg(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    hhh=models.ForeignKey(fff,on_delete=models.CASCADE)
    body=models.TextField()
    time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]