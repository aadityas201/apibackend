from django.contrib import admin
from django.urls import path, include
from repoinfo.views import *

urlpatterns = [
    path('', repInfo.as_view(), name = 'repoinfo'),
    path('languages' , langauges.as_view(), name = "repoLanguages" )
    
]