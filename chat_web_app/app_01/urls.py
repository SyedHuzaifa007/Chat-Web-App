from django.conf.urls import url
from django.contrib import admin
# This file is created by me ===> 007

from django.urls import include, path
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('',include('chat.urls')),
    path('admin/', admin.site.urls),
]