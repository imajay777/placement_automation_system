from __future__ import unicode_literals
from django.db import models
from time import time


def get_upload_filename(instance,filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)


def get_upload_imagename(instance,filename):
    return "credentials/dist/img/%s" % (filename)
# Create your models here.
  

class contact(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=20)
    mobile=models.IntegerField(null=True)
    temporary_address=models.CharField(max_length=20)
    permanent_address=models.CharField(max_length=20,null=True)
    website=models.CharField(max_length=20)
    upload_cv=models.FileField(upload_to=get_upload_filename,null=True)
   
class internships(models.Model):
    username=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=20)
    field1=models.CharField(max_length=200,null=True)
    field2=models.CharField(max_length=200)
    field3=models.CharField(max_length=200,null=True)
    
class postgrad(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class undergrad(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    Last_spi=models.FloatField(max_length=10)
    Cpi=models.FloatField(max_length=10)
    Branch_of_study=models.CharField(max_length=20)

class srsec(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    percentage_obtained=models.FloatField(max_length=10)
    school=models.CharField(max_length=10)
    Board=models.CharField(max_length=20)
    
class sec(models.Model):
    username=models.CharField(max_length=20)
    yearofpassing=models.IntegerField()
    percentage_or_cpi=models.FloatField(max_length=10)
    school=models.CharField(max_length=10)
    Board=models.CharField(max_length=20)
    
class languages(models.Model):
    username=models.CharField(max_length=20)
    languages_known=models.CharField(max_length=40)   
    
class projects(models.Model):
    username=models.CharField(max_length=20)
    title=models.CharField(max_length=40)
    position=models.CharField(max_length=40)
    duration=models.CharField(max_length=40)
    description=models.CharField(max_length=200)
    projects_related_url=models.CharField(max_length=50)
    
class photo(models.Model):
    username=models.CharField(max_length=20)
    imagename=models.CharField(max_length=50,null=True)
    upload=models.ImageField(upload_to=get_upload_imagename,null=True)

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')    