from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Developer, Skill
# Create your views here.


class DevelopersList(ListView):
    model = Developer
    context_object_name = 'developers'
    template_name = "developers/developers_list.html"


class DevelopersDetail(DetailView):
    model = Developer
    template_name = "developers/developer_detail.html"
    context_object_name = "developer"
