from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

# Create your views here.


class ProjectsList(LoginRequiredMixin, ListView):
    model = Project
    template_name = "project/projects_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print("MESSAGES:", [
              m.message for m in messages.get_messages(self.request)])
        return context


class ProjectDetail(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "project/project_detail.html"
    context_object_name = "project"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Project, pk=pk)


# class CreateProject(LoginRequiredMixin, CreateView):
#     model = Project
#     form_class = ProjectForm
#     template_name = "project/project_form.html"
#     success_url = "/projects/"

#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         context = self.get_context_data()
#         form.save()
#         messages.success(self.request, "project added successfully!!!")
#         return super().form_valid(form)

@permission_required(perm=['project.add_project'], login_url='accounts:login')
def CreateProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('projects:project_list')
    else:
        form = ProjectForm()
        return render(request, template_name="project/project_form.html", context={'form': form})


class DeleteProject(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = "project/project_detail.html"
    success_url = reverse_lazy("projects:project_list")
    raise_exception = False
    permission_required = "project.delete_project"
    permission_denied_message = "you don't have access to delete this project"
    login_url = 'accounts:login'

    def handle_no_permission(self):
        messages.error(
            self.request, "you don't have access to delete this project")
        return redirect('projects:project_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "project deleted successfully!!!")
        return super().delete(request, *args, **kwargs)


# --------------------------------------------------------------------------------

# this  decorator  checks that user is owner or have access to this view or not


def owner_or_have_permission(model, perm=None):
    def decorator(view_fun):
        @wraps(view_fun)
        def wrapper(request, *arge, **kwargs):
            user = request.user
            obj = get_object_or_404(model, pk=kwargs.get('pk'))
            if getattr(obj, name="owner"):
                return view_fun(request, *arge, **kwargs)

            if user.has_perm(perm):
                return view_fun(request, *arge, **kwargs)

            raise PermissionDenied(
                "You do not have permission to access this.")
        return wrapper
    return decorator


# ---------------------------------------------------------------------------------

class UpdateProject(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "project/project_updateform.html"
    success_url = "/projects/"

    def form_valid(self, form):
        messages.success(self.request, "project updated successfully!!")
        return super().form_valid(form)
