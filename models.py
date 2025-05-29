from django.db import models

class user(models.Model):
    fullname = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    password = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100,blank=True)




