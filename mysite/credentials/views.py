from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import studentform
from .models import contact
# Create your views here.



def contact(request):
    f=studentform(request.POST)
    if f.is_valid():
        
        new=f.save(commit=False)
        
        #new.lastname='prodhan'
        # firstname=f.cleaned_data['firstname']
        #new_join, created=student.objects.get_or_create(firstname=firstname)
        new.save()
    context={"form":f}
    template="contact.html"
    return render(request,template,context)
