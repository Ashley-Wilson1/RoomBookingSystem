from django.db import models
from django.contrib.auth.models import User
 

 #Make sure to make the databases information correct
class ROOMS(models.Model):
    id = models.AutoField(primary_key=True,)
    capacity = models.CharField(max_length=10)

class ROOMBOOKING(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=25)
    date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class USERS(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    firstname = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
