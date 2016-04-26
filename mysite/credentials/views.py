from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactform,internshipform,languageform,projectform,postgradform,undergradform,srsecform,secform,DocumentForm,photoform,overviewform,statisticsform,jobprofileform,benefitsform,logoform,mediaform,headofficeform,Workform,Sales_officeform
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
import cgi
from cs243.view import piconce
# Create your views here.
global field1,field2,field3,yopp,spip,cpip,branch,yopu,spiu,cpiu,board,school,perc,boardsc,schoolsc,percsc,yopsc,yopsr,l,pr1,pr2,pr3,f1,f2,f3


def search(request):
    context={}
    template="search.html"
    return render(request,template,context)

def studentsearch(request):
    data = contact.objects.filter(username=request.POST['studentsearch'])
    if len(data)>0:
        p=photo.objects.filter(username=request.POST['studentsearch'])
        i=internships.objects.filter(username=request.POST['studentsearch'])
        if len(i)>0:
            f1=i[0].field1
            f2=i[0].field2
            f3=i[0].field3
        else:
            f1=''
            f2=''
            f3=''
        # post=postgrad.objects.filter(username=request.POST['studentsearch'])
        # if len(post)>0:
        #     yopp=post[0].year_of_passing
        #     spip=post[0].Last_spi
        #     cpip=post[0].Cpi
        #     branch=post[0].Branch_of_study
        # else:
        #     yopp=''
        #     spip=''
        #     cpip=''
        #     branch=''
        # under=undergrad.objects.filter(username=request.POST['studentsearch'])
        # if len(under)>0:
        #     yopu=under[0].year_of_passing
        #     spiu=under[0].Last_spi
        #     cpiu=under[0].Cpi
        #     
        # else:
        #     yopu=''
        #     spiu=''
        #     cpiu=''
        # sr=srsec.objects.filter(username=request.POST['studentsearch'])
        # if len(sr)>0:
        #     yopsr=sr[0].year_of_passing
        #     perc=sr[0].percentage_obtained
        #     school=sr[0].school
        #     board=sr[0].board
        # else:
        #     yopsr=''
        #     perc=''
        #     school=''
        #     board=''   
        # sc=sec.objects.filter(username=request.POST['studentsearch'])
        # if len(sc)>0:
        #     yopsc=sc[0].year_of_passing
        #     percsc=sc[0].percentage_obtained
        #     schoolsc=sc[0].school
        #     boardsc=sc[0].board
        # else:
        #     yopsc=''
        #     percsc=''
        #     schoolsc=''
        #     boardsc=''
        # lang=language.objects.filter(username=request.POST['studentsearch'])
        # if len(lang)>0:
        #     l=lang[0].languages_known
        # else:
        #     l=''
        # pr=projects.objects.filter(username=request.POST['studentsearch'])
        # if len(sc)>0:
        #     pr1=pr[0].project1
        #     pr2=pr[0].project2
        #     pr3=pr[0].project3
        # else:
        #     pr1=''
        #     pr2=''
        #     pr3=''
            
            
        #context={'name':request.POST['studentsearch'],'l':l,'picname':p[0].imagename,'pr1':pr1,'pr2':pr2,'pr3':pr3,'yopsr':yopsr,'yopsc':yopsc,'percsc':percsc,'perc':perc,'schoolsc':schoolsc,'boardsc':boardsc,'school':school,'board':board,'yopu':yopu,'cpiu':cpiu,'spiu':spiu,'yopp':yopp,'cpip':cpip,'spip':spip,'branch':branch,'f1':field1,'f2':field2,'f3':field3,'email':data[0].email,'mob':data[0].mobile,'temp':data[0].temporary_address,'per':data[0].permanent_address}
        context={'name':request.POST['studentsearch'],'picname':p[0].imagename,'f1':f1,'f2':f2,'f3':f3,'email':data[0].email,'mob':data[0].mobile,'temp':data[0].temporary_address,'per':data[0].permanent_address}
        template="studentsearch.html"
        return render(request,template,context)

def contactview(request):
    language='en-gb'
    session_language= 'en-gb'
    
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
            
    data = contact.objects.filter(username=request.user.username)
    if len(data)==0:
         # Handle file upload
        if request.method == 'POST':
            
            f=contactform(request.POST,request.FILES)
            if f.is_valid():
                newdoc=f.save(commit=False)
                newdoc.upload_cv=request.FILES['upload_cv']
                newdoc.username = request.user.username
                #newdoc = contact(upload_cv = request.FILES['upload_cv'])
                #newdoc = contact(username = request.user.username)
                newdoc.save()

            context={"form":f,"language":language,"session_language":session_language,'picname':piconce}
            template="contact.html"
            return render(request,template,context,context_instance=RequestContext(request))
        else:
            f=contactform()
            return render(request,"contact.html",{"form":f,"language":language,"session_language":session_language,'picname':piconce},context_instance=RequestContext(request))
    else:
        obj=contact.objects.filter(username=request.user.username)
        t=get_template("profile_contact.html")
        p=t.render(Context({'fullname':request.user.username,'obj':obj[0],'picname':piconce,'email':request.user.email,'mobile':data[0].mobile,'temp':data[0].temporary_address,'perm':data[0].permanent_address,'website':data[0].website}))
        return HttpResponse(p)
    

def language(request,language='en-gb'):
    response = HttpResponse("setting languages to %s" % language)
    
    response.set_cookie('lang',language)
    
    request.session['lang'] = language
    
    return response


def internshipview(request):
    f2=internshipform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()

    context={"form2":f2,'picname':''}
    template="internships.html"
    return render(request,template,context)

def postgradview(request):
    f2=postgradform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="postgrad.html"
    return render(request,template,context)

def undergradview(request):
    f2=undergradform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="undergrad.html"
    return render(request,template,context)

def srsecview(request):
    f2=srsecform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="srsec.html"
    return render(request,template,context)

def secview(request):
    f2=secform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="sec.html"
    return render(request,template,context)

def languageview(request):
    f2=languageform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="languages.html"
    return render(request,template,context)

def projectview(request):
    f2=projectform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="projects.html"
    return render(request,template,context)

def photoview(request):
    
    data = photo.objects.filter(username=request.user.username)
    if len(data)==0:
        
        f=photoform(request.POST,request.FILES)
        if f.is_valid():
        
            new=f.save(commit=False)
            new.username=request.user.username
            new.imagename=request.FILES['upload'].name
            print new.imagename
            new.save()
        context={"form":f,'picname':piconce}
        template="photo.html"
        return render(request,template,context)
    
    else:
        t=get_template("profile_photo.html")
        p=t.render(Context({"fullname":request.user.username,"picname":data[0].imagename}))
        return HttpResponse(p)



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('credentials.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form,'picname':piconce},
        context_instance=RequestContext(request)
    )

def clist(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('credentials.views.clist'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'clist.html',
        {'documents': documents, 'form': form,'picname':piconce},
        context_instance=RequestContext(request)
    )

##company views

def jobprofile(request):
    f2=jobprofileform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="jobprofile.html"
    return render(request,template,context)

def logo(request):
    f2=logoform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="logo.html"
    return render(request,template,context)

def headoffice(request):
    f2=headofficeform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="headoffice.html"
    return render(request,template,context)

def statistics(request):
    f2=statisticsform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="statistics.html"
    return render(request,template,context)

def work(request):
    f2=Workform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="works.html"
    return render(request,template,context)

def media(request):
    f2=mediaform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="media.html"
    return render(request,template,context)

def salesoffice(request):
    f2=Sales_officeform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="salesoffice.html"
    return render(request,template,context)

def benefits(request):
    f2=benefitsform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="benefits.html"
    return render(request,template,context)


def overview(request):
    f2=overviewform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="overview.html"
    return render(request,template,context)

