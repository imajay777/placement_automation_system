from django.contrib import admin
from credentials.models import student,company,contact,internships
# Register your models here.
admin.site.register(student)
admin.site.register(company)
admin.site.register(contact)
admin.site.register(internships)
