from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import Developer, Skill
from .forms import *
# Create your views here.


class DevelopersList(ListView):
    model = Developer
    context_object_name = 'developers'
    template_name = "developers/developers_list.html"

    def get_queryset(self):
        return Developer.objects.all()


class DevelopersDetail(DetailView):
    model = Developer
    template_name = "developers/developer_detail.html"
    context_object_name = "developer"

    def get_object(self, queryset=...):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Developer, pk=pk)


class DevelopersCreation(CreateView):
    model = Developer
    form_class = DeveloperForm
    template_name = "developers/developer_form.html"
    success_url = "/developers/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["skillForm"] = Skill_formset(self.request.POST)
        else:
            context["skillForm"] = Skill_formset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        skillForm = context["skillForm"]

        if skillForm.is_valid():
            dev = form.save()
            skillForm.instance = dev
            skillForm.save()
            messages.success(self.request, "Developer added successfully!!")
            return super().form_valid(form)


class UpdateDevelopers(UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = "developers/developer_updateform.html"
    success_url = "/developers/"
    context_object_name = 'developers'

    def form_valid(self, form):

        messages.success(self.request, "Developer updated successfully!!")
        return super().form_valid(form)


class DeleteDevelopers(DeleteView):
    model = Developer
    template_name = "developers/developer_detail.html"
    success_url = "/developers/"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "developers deleted successfully!!!")
        return super().delete(request, *args, **kwargs)
