from django.contrib import admin
from credentials.models import Document,PLACEMENTS_DATA,contact,internship,postgrad,undergrad,srsec,sec,language,project,photo,overview,jobprofile,benefits,logo,media,headoffice,Work,Sales_office
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
admin.site.register(Document)
#admin.site.register(UserProfile)
#admin.site.register(search)

