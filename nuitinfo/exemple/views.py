from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import Template, Context, loader
from .models import Task, User, Email, DiffusionList


def home(request):
    tasks_list = Task.objects.order_by("name")
    users_list = User.objects.order_by("lastname")
    diffusion_lists_list = DiffusionList.objects.order_by("name")
    context = {
        "tasks_list": tasks_list,
        "users_list": users_list,
        "diffusion_lists_list": diffusion_lists_list,
    }
    return render(request, "exemple/index.html", context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    doers = User.objects.filter(tasks__id=task_id)
    context = {
        "task": task,
        "doers": doers,
    }
    return render(request, "exemple/task_details.html", context)


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = Task.objects.filter(doers__id=user_id)
    email = Email.objects.filter(user__id=user_id).first()  # .first() pour
    # transformer le queryset en object unique de classe Email
    context = {
        "user": user,
        "tasks": tasks,
        "email": email,
    }
    return render(request, "exemple/user_details.html", context)


def diffusion_list_detail(request, diffusion_list_id):
    diffusion_list = get_object_or_404(DiffusionList, id=diffusion_list_id)
    users = User.objects.filter(email__diffusion_list=diffusion_list)
    context = {
        "diffusion_list": diffusion_list,
        "users": users,
    }
    return render(request, "exemple/diffusion_list_details.html",
                  context)
