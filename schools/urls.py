from django.urls import path, include
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('<str:slug>/', school, name='school-detail'),
    path('all-schools/', allSchools, name='all-schools'),
    path('favs/', favs, name='favs'),
    # path('', SchoolListView.as_view(), name='schools'),
    # path('<str:slug>/', SchoolDetailView.as_view(),
    #      name='school-detail'),
]
