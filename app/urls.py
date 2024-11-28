from . import views
from django.urls import path


# Create your views here.
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),
    path('curso/<int:id>/', views.curso, name='curso'),
    path('tema/<int:id>/', views.tema, name='tema'),
    path('tablero', views.tablero, name='tablero'),
    path('tablero/mis-cursos', views.mis_cursos, name='mis-cursos'),
    path('tablero/mis-notas', views.mis_notas, name='mis-notas'),
    path('tablero/mis-preferencias', views.mis_preferencias, name='mis-preferencias'),
    path('suscribir', views.suscribir, name='suscribir'),
]

