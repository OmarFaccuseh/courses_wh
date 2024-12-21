from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Curso, Tema, Profile, Nota
from .forms import NotaForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages




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


def desuscribir (request):
    curso_id = request.POST.get('curso_id')
    profile = Profile.objects.get(user=request.user.id)
    profile.cursos.remove(curso_id)
    return redirect('app:tablero')


def deleteNota(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    nota.delete()
    return redirect('app:tablero')

'''
def suscribir(request):
    curso_id = request.GET.get('curso_id') 
    profile = Profile.objects.get(user=request.user.id)
    if profile and curso_id :
        profile.cursos.add(curso_id)
        return JsonResponse({'ok': True})
    return JsonResponse({'ok': False})

'''

def inicio(request):
    return render(request, 'inicio.html')


@login_required(login_url='accounts/login/')
def mis_cursos(request):
    profile = Profile.objects.get(user=request.user.id)
    cursos = profile.cursos.all()
    context = {'cursos': cursos}
    return render(request, 'tablero/partials/cursos_tablero.html', context)


@login_required(login_url='accounts/login/')
def misNotas(request):
    profile = Profile.objects.get(user=request.user.id)
    notas = Nota.objects.filter(perfil=profile.id)

    notaFormSet = modelformset_factory(Nota, form=NotaForm, extra=1)
    if request.method == 'POST':
        formset = notaFormSet(request.POST, queryset=notas)

        if formset.is_valid():
            new_notas = formset.save(commit=False)
            for nota in new_notas:
                if not nota.pk:
                    nota.perfil = profile
                nota.save()
            return render(request, "tablero/tablero.html", {'formset': formset, 'section':'notas'})
        else:
            for form in formset:
                if form.errors:
                    print(form.errors)
                    errors = form.errors
            messages.error(request, "Error al guardar nota")
            print('merch')
            return render(request, "tablero/tablero.html", {'formset': formset, 'section':'notas'})

    else:
        formset = notaFormSet(queryset=notas)
    return render(request, "tablero/partials/notas.html", {'formset': formset})


@login_required(login_url='accounts/login/')
def mis_preferencias(request):
    return render(request, 'tablero/partials/preferencias.html')


'''
# for Stripe
def stripe_success(request):
    return HttpResponse(f"Compra finalizada :) {True}")


# for Stripe
def stripe_cancel(request):
    return HttpResponse(f"Compra cancelada :( ")
'''


