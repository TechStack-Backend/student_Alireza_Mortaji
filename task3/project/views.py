from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Project
from .forms import ProjectForm
from django.contrib import messages


# Create your views here.


class ProjectsList(ListView):
    model = Project
    template_name = "project/projects_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetail(DetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)

# def createProject(request):
#     if request.method == "POST":
#         projectForm = ProjectForm(request.POST)
#         if projectForm.is_valid():
#             projectForm.save()
#             return redirect("projects:project_list")
#     elif request.method == "GET":
#         projectForm = ProjectForm()

#     return render(request, "project/project_form.html", context={"form": projectForm})


class CreateProject(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_form.html"
    success_url = "projects:project_list"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        context = self.get_context_data()
        form.save()
        messages.success(self.request, "project added successfully!!!")
        return redirect(self.success_url)


class DeleteProject(DeleteView):
    model = Project
    template_name = "project/project_detail.html"
    success_url = "/projects/"

    def delete(self, request, *args, **kwargs):
        messages.success("project deleted successfully!!!")
        return super().delete(request, *args, **kwargs)
