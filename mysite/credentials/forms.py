from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import contact,internships


    
    
class contactform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=contact
        fields=['mobile','temporary_address','permanent_address','website']
    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        return email
    
    
class internshipsform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=internships
        fields=['field1','field2','field3']
        
