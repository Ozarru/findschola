from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('my_school/', mySchoolView, name='my_school'),
    path('add_school/', addSchoolView, name='add_school'),
    path('dashboard/', dashView, name='dashboard'),
    path('<str:slug>/', school, name='school-detail'),
    # path('', SchoolListView.as_view(), name='schools'),
    # path('<str:slug>/', SchoolDetailView.as_view(),
    #      name='school-detail'),
]
