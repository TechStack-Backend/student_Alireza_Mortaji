from django.contrib import admin
from django.urls import path
from .views import DevelopersListView, DeveloperCV_View

urlpatterns = [
    path('developers/', DevelopersListView, name='DevelopersList'),
    path('developers/<str:username>/', DeveloperCV_View, name='Developer_cv')
]
