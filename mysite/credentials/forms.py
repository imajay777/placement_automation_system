from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import contact

# class EmailForm(forms.Form):
#     firstname=forms.CharField(max_length=20)
#     lastname=forms.CharField()
#     email= forms.EmailField()
#     mobile=forms.IntegerField()
#     temporary_address=forms.CharField()
#     permanent_address=forms.CharField()
    
    
class studentform(forms.ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        model=contact
        fields=['email','mobile','temporary_address','permanent_address','website']
    