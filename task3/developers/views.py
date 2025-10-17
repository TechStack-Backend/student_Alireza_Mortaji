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
            return redirect(self.success_url)


# def createDevelopers(request):
#     if request.method == "POST":
#         developerForm = DeveloperForm(request.POST)
#         skillForm = Skill_formset(request.POST)
#         if developerForm.is_valid() and skillForm.is_valid():
#             dev = developerForm.save()
#             skillForm.instance = dev
#             skillForm.save()
#             return redirect("developers:developer_list")
#     elif request.method == "GET":
#         developerForm = DeveloperForm()
#         skillForm = Skill_formset()

#     return render(request, template_name="developers/developer_form.html", context={"form": developerForm, "skillForm": skillForm})


class UpdateDevelopers(UpdateView):
    model = Developer
    form_class = DeveloperForm
    template_name = "developers/developer_form.html"
    success_url = "developers/"


class DeleteDevelopers(DeleteView):
    model = Developer
    template_name = "developers/developer_detail.html"
    success_url = "/developers/"

    def delete(self, request, *args, **kwargs):
        messages.success("developers deleted successfully!!!")
        return super().delete(request, *args, **kwargs)
