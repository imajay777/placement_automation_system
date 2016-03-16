from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.IntegerField()
    
class company(models.Model):
    cname=models.CharField(max_length=30)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mobile=models.IntegerField()    
    
class contact(models.Model):
    email=models.CharField(max_length=20)
    mobile=models.IntegerField(null=True)
    temporary_address=models.CharField(max_length=20)
    permanent_address=models.CharField(max_length=20,null=True)
    website=models.CharField(max_length=20)
   
class internships(models.Model):
    email=models.CharField(max_length=20)
    field1=models.CharField(max_length=200,null=True)
    field2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200,null=True)
    #website=models.CharField(max_length=20)    
