
  
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^location/(?P<location_name>\w+)',views.location,name = 'location'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)