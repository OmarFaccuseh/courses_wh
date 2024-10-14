from django.shortcuts import render
from . import views
from django.urls import path


# Create your views here.
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),

]

