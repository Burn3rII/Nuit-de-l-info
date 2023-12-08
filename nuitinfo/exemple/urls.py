from django.urls import path
from . import views

app_name = "exemple"
urlpatterns = [
    path("home", views.home, name="home"),
]
