"""cs243 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from cs243.view import login,index2,studentprofile,postgrad,undergrad,srsec,sec,languages,projects,ex
from credentials.views import internships,contactview,language,photoview
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#      url(r'^login/$', login),
#       url(r'^index2/$', index2),
#        url(r'^studentprofile/$', studentprofile),
#         url(r'^photo/$', photo),
#           url(r'^postgrad/$', postgrad),
#           url(r'^undergrad/$', undergrad),
#           url(r'^srsec/$', srsec),
#           url(r'^sec/$', sec),
#           url(r'^internships/$', internships),
#           url(r'^languages/$', languages),
#           url(r'^contact/$', contactview),
#           url(r'^projects/$', projects),
#           url(r'^language/(?P<language>[a-z\-]+)/$', language),
#           url(r'^auth/$', 'cs243.view.auth_view'),
#           url(r'^invalid/$', 'cs243.view.invalid_login'),
#           url(r'^loggedin/$', 'cs243.view.loggedin'),
#           url(r'^register/$', 'cs243.view.register_user'),
#           url(r'^register_success/$', 'cs243.view.register_success'),
#           url(r'^profile_contact/$', 'cs243.view.profile_contact'),
#           url(r'file:///C:/Users/Sagar Roy Prodhan/Desktop/cs243/mysite/credentials/media/uploaded_files/1460525607_91_CV_Sagar_Roy_Prodhan.pdf$', ex),
# 
# 
# ]

    
    
urlpatterns = patterns('',
     (r'^', include('credentials.urls')),(r'^admin/', admin.site.urls),
     (r'^login/$', login),
      (r'^index2/$', index2),
       (r'^studentprofile/$', studentprofile),
       (r'^photo/$', photoview),
       (r'^profile_photo/$', 'cs243.view.profile_photo'),
          (r'^postgrad/$', postgrad),
          (r'^undergrad/$', undergrad),
          (r'^srsec/$', srsec),
          (r'^sec/$', sec),
          (r'^internships/$', internships),
          (r'^languages/$', languages),
          (r'^contact/$', contactview),
          (r'^projects/$', projects),
          (r'^language/(?P<language>[a-z\-]+)/$', language),
          (r'^auth/$', 'cs243.view.auth_view'),
          (r'^invalid/$', 'cs243.view.invalid_login'),
          (r'^loggedin/$', 'cs243.view.loggedin'),
          (r'^register/$', 'cs243.view.register_user'),
          (r'^register_success/$', 'cs243.view.register_success'),
          (r'^profile_contact/$', 'cs243.view.profile_contact'),
          (r'file:///C:/Users/Sagar Roy Prodhan/Desktop/cs243/mysite/credentials/media/uploaded_files/1460525607_91_CV_Sagar_Roy_Prodhan.pdf$', ex),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)