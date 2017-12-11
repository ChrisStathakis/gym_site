from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name = "projects"

urlpatterns = [
    url(r'^$', ProjectView.as_view(), name='home'),
    url(r'details/(?P<slug>[-\w]+)/$', ProjectDetailView.as_view(), name='view'),
    ]
