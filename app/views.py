from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso


def cursos(request):
    qs = Curso.objects.all()
    context = {'courses': qs}

    return render(request, 'courses.html', context)


def inicio(request):
    return render(request, 'inicio.html')





