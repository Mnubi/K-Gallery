
  
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.homepage,name='home'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^location/(?P<location_name>\w+)',views.get_image_location,name = 'location'),
    url('^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)