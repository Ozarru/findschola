from django.urls import path, include
from .views import *

# app_name = 'base'
urlpatterns = [
    path('', blogView, name='blog'),
]
