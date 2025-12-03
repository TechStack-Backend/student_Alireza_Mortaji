from django.contrib import admin
from django.urls import path
from .views import *


app_name = "projects"

urlpatterns = [
    path('', ProjectsList.as_view(), name="project_list"),
    path("<int:pk>", ProjectDetail.as_view(), name="project_detail"),
    path("create", CreateProject.as_view(), name="project_create"),
    path("delete/<int:pk>", DeleteProject.as_view(), name="delete_project"),
    path("update/<int:pk>", UpdateProject.as_view(), name="update_project")
]
