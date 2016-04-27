from django.contrib import admin
from credentials.models import PLACEMENTS_DATA,contact,internship,postgrad,undergrad,srsec,sec,language,project,photo,overview,jobprofile,benefits,logo,media,headoffice,Work,Sales_office



"""
# Extending User model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from models import Extra_Info


 #Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Extra_InfoInline(admin.TabularInline):
    model = Extra_Info
    can_delete = False
    verbose_name_plural = 'Extra_info'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Extra_InfoInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

"""









# Register your models here.

admin.site.register(contact)
admin.site.register(postgrad)
admin.site.register(undergrad)
admin.site.register(srsec)
admin.site.register(sec)
admin.site.register(internship)
admin.site.register(language)
admin.site.register(project)
admin.site.register(photo)
admin.site.register(overview)
admin.site.register(jobprofile)
admin.site.register(benefits)
admin.site.register(logo)
admin.site.register(media)
admin.site.register(headoffice)
admin.site.register(Work)
admin.site.register(Sales_office)
admin.site.register(PLACEMENTS_DATA)
#admin.site.register(search)

