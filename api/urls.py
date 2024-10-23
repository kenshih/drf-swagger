from django.urls import path
from api import views

urlpatterns = [
    path('', views.FilmList.as_view()),
]