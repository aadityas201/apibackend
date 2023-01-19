from django.contrib import admin
from django.urls import path, include
from userinfo.views import *

urlpatterns = [
    path('', userInfo.as_view(), name = 'userinfo')
]