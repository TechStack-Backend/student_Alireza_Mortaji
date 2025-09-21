from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def Home(request):
    if request.method == "GET":
        return HttpResponse('hello world Alireza Mortaji')
