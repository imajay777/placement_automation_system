from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.



def login(request, template='index2.html'):
    return HttpResponseRedirect('/index2/')
