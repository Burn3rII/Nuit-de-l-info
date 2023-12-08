from django.urls import path
from . import views

app_name = "quizz"
urlpatterns = [
    path("home", views.home, name="home"),
    path("questiondetail/<int:question_id>/", views.detail, name="detail"),
    path('results/<int:question_id>/<str:is_correct>/', views.results,
         name='results'),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
