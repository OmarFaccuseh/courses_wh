from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Tema, Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def cursos(request):
    qs = Curso.objects.all()
    courses_values = Curso.objects.all().values('id', 'name', )
    courses_with_url = [
        {**course, 'get_absolute_url': course.get('get_absolute_url'),
         } for course in courses_values
    ]
    context = {'courses': qs, 'courses_values': courses_with_url}

    return render(request, 'courses.html', context)


def curso(request, id=None):
    curso = Curso.objects.get(id=id)
    temas = curso.tema_set.all()
    logueado = request.user.is_authenticated
    profile = Profile.objects.get(user=request.user.id) if logueado else False
    suscrito = (id in profile.cursos.values_list('id', flat=True)) if logueado else False
    
    context = {'curso': curso, 
               'temas': temas, 
               'suscrito': suscrito,
               'logueado': logueado
               }
    
    return render(request, 'course.html', context)


def tema(request, id=None):
    tema = Tema.objects.get(id=id)
    temas = Tema.objects.filter(curso=tema.curso)
    context = {'tema': tema,
               'temas': temas
               }

    return render(request, 'tema.html', context)


@login_required(login_url='accounts/login/')
def tablero(request):
    profile = Profile.objects.get(user=request.user.id)
    cursos = profile.cursos.all()
    context = {'cursos': cursos}

    return render(request, 'tablero/tablero.html', context)


def suscribir(request):
    curso_id = request.GET.get('curso_id')
    profile = Profile.objects.get(user=request.user.id)
    if profile and curso_id :
        profile.cursos.add(curso_id)
        return JsonResponse({'ok': True})
    return JsonResponse({'ok': False})


def inicio(request):
    return render(request, 'inicio.html')


@login_required(login_url='accounts/login/')
def mis_cursos(request):
    profile = Profile.objects.get(user=request.user.id)
    cursos = profile.cursos.all()
    context = {'cursos': cursos}
    return render(request, 'tablero/partials/cursos_tablero.html', context)


@login_required(login_url='accounts/login/')
def mis_notas(request):
    profile = Profile.objects.get(user=request.user.id)
    notas = profile.notas.all()
    context = {'notas': notas}
    return render(request, 'tablero/partials/notas.html', context=context)


@login_required(login_url='accounts/login/')
def mis_preferencias(request):
    return render(request, 'tablero/partials/preferencias.html')







