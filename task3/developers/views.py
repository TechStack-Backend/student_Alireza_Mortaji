from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import Developer, Skill
from .forms import *
# Create your views here.


class DevelopersList(ListView):
    model = Developer
    context_object_name = 'developers'
    template_name = "developers/developers_list.html"


class DevelopersDetail(DetailView):
    model = Developer
    template_name = "developers/developer_detail.html"
    context_object_name = "developer"


def createDevelopers(request):
    if request.method == "POST":
        developerForm = DeveloperForm(request.POST)
        skillForm = Skill_formset(request.POST)
        if developerForm.is_valid() and skillForm.is_valid():
            dev = developerForm.save()
            skillForm.instance = dev
            skillForm.save()
            return redirect("developers:developer_list")
    elif request.method == "GET":
        developerForm = DeveloperForm()
        skillForm = Skill_formset()

    return render(request, template_name="developers/developer_form.html", context={"form": developerForm, "skillForm": skillForm})
