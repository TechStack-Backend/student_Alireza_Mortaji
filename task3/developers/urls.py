from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'developers'

urlpatterns = [
    path('', DevelopersList.as_view(), name="developer_list"),
    path("<int:pk>", DevelopersDetail.as_view(), name="developer_detail"),
    path("create", DevelopersCreation.as_view(), name="create_developers"),
    path("delete/<int:pk>", DeleteDevelopers.as_view(), name="delete_developer")
]
