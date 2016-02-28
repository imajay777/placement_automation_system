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

def photo(request):
    t=get_template("photo.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def contact(request):
    t=get_template("contact.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def postgrad(request):
    t=get_template("postgrad.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def srsec(request):
    t=get_template("srsec.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def sec(request):
    t=get_template("sec.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def undergrad(request):
    t=get_template("undergrad.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def internships(request):
    t=get_template("internships.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def languages(request):
    t=get_template("languages.html")
    p=t.render(Context({}))
    return HttpResponse(p)

def projects(request):
    t=get_template("projects.html")
    p=t.render(Context({}))
    return HttpResponse(p)





