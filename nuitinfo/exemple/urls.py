from django.urls import path
from . import views

app_name = "exemple"
urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_details"),
    path("users/<int:user_id>/", views.user_detail, name="user_details"),
    path("diffusion_lists/<int:diffusion_list_id>/",
         views.diffusion_list_detail, name="diffusion_list_details"),
]
