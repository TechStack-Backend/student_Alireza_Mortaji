from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'developers'

urlpatterns = [
    path('developers/', DevelopersList.as_view(), name="developer_list"),
    path("developers/<int:pk>", DevelopersDetail.as_view(), name="developer_detail"),
    path("developers/create", createDevelopers, name="create_developers")
]
