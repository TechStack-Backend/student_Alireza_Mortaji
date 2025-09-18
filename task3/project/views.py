from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project


# Create your views here.


class ProjectsList(ListView):
    model = Project
    template_name = "project/projects_list.html"
    context_object_name = "projects"


class ProjectDetail(DetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"
