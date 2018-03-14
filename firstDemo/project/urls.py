from django.conf.urls import url  
from django.contrib import admin  
from jdango_Second.views import showInfo  
  
urlpatterns = [  
    url(r'^admin/',admin.site.urls),  
    url(r'^index/',showInfo),  
]  