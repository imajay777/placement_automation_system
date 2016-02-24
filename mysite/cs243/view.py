from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def login(request):
    t=get_template("login.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def index2(request):
    t=get_template("index2.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def studentprofile(request):
    t=get_template("studentprofile.html")
    p=t.render(Context({}))
    return HttpResponse(p)