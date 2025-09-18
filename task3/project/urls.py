from django.contrib import admin
from django.urls import path
from .views import *


app_name = "projects"

urlpatterns = [
    path('projects/', ProjectsList.as_view(), name="project_list"),
    path("projects/<int:pk>", ProjectDetail.as_view(), name="project_detail")
]
