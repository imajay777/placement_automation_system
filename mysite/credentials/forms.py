from django import forms
from django.forms import ModelForm,Textarea
from django.core.exceptions import NON_FIELD_ERRORS
from .models import contact,internships,photo,overview
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    student_company=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2','student_company']
        
    def save(self,commit=True):
        user=super(MyRegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.student_company=self.cleaned_data['student_company']
        if commit:
            user.save()
        return user    
    
    
    

    
    
class contactform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=contact
        widgets={'email':Textarea(attrs={'placeholder':'email','cols': 80, 'rows': 1}),'mobile':Textarea(attrs={'placeholder':'mobile','cols': 80, 'rows': 1}),'temporary_address':Textarea(attrs={'placeholder':'temporary_address','cols': 80, 'rows': 3}),'permanent_address':Textarea(attrs={'placeholder':'permanent address','cols': 80, 'rows': 3}),'website':Textarea(attrs={'placeholder':'link','cols': 80, 'rows': 1}),}
        fields=['email','mobile','temporary_address','permanent_address','website','upload_cv']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        return email
    

class photoform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=photo
        ###widgets={'email':Textarea(attrs={'placeholder':'email','cols': 80, 'rows': 1}),'mobile':Textarea(attrs={'placeholder':'mobile','cols': 80, 'rows': 1}),'temporary_address':Textarea(attrs={'placeholder':'temporary_address','cols': 80, 'rows': 3}),'permanent_address':Textarea(attrs={'placeholder':'permanent address','cols': 80, 'rows': 3}),'website':Textarea(attrs={'placeholder':'link','cols': 80, 'rows': 1}),}
        fields=['upload']
    


    
class internshipsform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=internships
        
        fields=['field1','field2','field3']
        

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    
    
###company forms

class overviewform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=overview
        
        fields=['description','url']
