from django.contrib import admin
from django.urls import path
from .views import DevelopersListView, DeveloperCV_View

urlpatterns = [
    path('', DevelopersListView, name='DevelopersList'),
    path('<str:username>/', DeveloperCV_View, name='Developer_cv')
]
