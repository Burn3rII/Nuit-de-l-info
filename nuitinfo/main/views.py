from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import Template, Context, loader


def home(request):
    context = {}
       
    return render(request, "main/index.html", context)


def infos(request):
    context = {}

    return render(request, "main/infos.html", context)
