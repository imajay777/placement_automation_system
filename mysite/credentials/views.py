from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactform,internshipsform,DocumentForm,photoform
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

# Create your views here.



def contactview(request):
    language='en-gb'
    session_language= 'en-gb'
    
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
    
    data = contact.objects.filter(username=request.user.username)
    if len(data)==0:
        
        f=contactform(request.POST,request.FILES)
        if f.is_valid():
        
            new=f.save(commit=False)
            new.username=request.user.username
        #new.email=user.email
        #new.lastname='prodhan'
        # firstname=f.cleaned_data['firstname']
        #new_join, created=student.objects.get_or_create(firstname=firstname)
            new.save()
        context={"form":f,"language":language,"session_language":session_language}
        template="contact.html"
        return render(request,template,context)
    
    else:
        t=get_template("profile_contact.html")
        p=t.render(Context({'fullname':request.user.username,'email':request.user.email,'mobile':data[0].mobile,'temp':data[0].temporary_address,'perm':data[0].permanent_address,'website':data[0].website}))
    
        return HttpResponse(p)
    

def language(request,language='en-gb'):
    response = HttpResponse("setting languages to %s" % language)
    
    response.set_cookie('lang',language)
    
    request.session['lang'] = language
    
    return response


def internships(request):
    f2=internshipsform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
  
    context={"form2":f2}
    template="internships.html"
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
        context={"form":f}
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
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )