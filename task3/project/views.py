from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Project
from .forms import ProjectForm


# Create your views here.


class ProjectsList(ListView):
    model = Project
    template_name = "project/projects_list.html"
    context_object_name = "projects"


class ProjectDetail(DetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"


def createProject(request):
    if request.method == "POST":
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid():
            projectForm.save()
            return redirect("projects:project_list")
    elif request.method == "GET":
        projectForm = ProjectForm()

    return render(request, "project/project_form.html", context={"form": projectForm})
