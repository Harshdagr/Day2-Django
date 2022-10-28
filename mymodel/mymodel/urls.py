
from django.contrib import admin 
from django.urls import path,re_path
from myApp.views import *

from django.conf import settings #add this
from django.conf.urls.static import static

from mymodel.settings import MEDIA_ROOT, MEDIA_URL #add this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/',start),
    path('',index,name='index'),
    # path("",include("image.urls")),

    re_path('delete/(\d+)',del_record,name='delete'),


    path('form_data/',create_data,name='form1' )
 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
