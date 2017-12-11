from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name = "blog"

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='home'),
    url(r'details/(?P<slug>[-\w]+)/$', BlogDetail.as_view(), name='view'),
    ]
