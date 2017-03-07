"""photogallary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from photos.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', photo_list, name='photo_list'),
    url(r'^photo_list_sort$', photo_list_sort, name='photo_list_sort'),
    url(r'^photo_upload/$', photo_upload ),
    url(r'^contact/$', contact ),
    url(r'^(?P<id>[0-9]+)/add_like/$', add_like, name='add_like'),
    url(r'^(?P<id>[0-9]+)/add_dislike/$', add_dislike, name='add_dislike'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #User  passpass12345
