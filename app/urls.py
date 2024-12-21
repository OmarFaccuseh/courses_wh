from . import views
from django.urls import path

app_name = 'app' 

# Create your views here.
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),
    path('curso/<int:id>/', views.curso, name='curso'),
    path('tema/<int:id>/', views.tema, name='tema'),
    path('tablero', views.tablero, name='tablero'),
    path('tablero/mis-cursos', views.mis_cursos, name='mis-cursos'),
    path('tablero/mis-notas', views.misNotas, name='mis-notas'),
    path('tablero/mis-preferencias', views.mis_preferencias, name='mis-preferencias'),
    path('desuscribir/', views.desuscribir, name='desuscribir'),
    path('delete_nota/<int:nota_id>/', views.deleteNota, name='delete_nota'),
    
    # path('suscribir/<int:cruso_id>', views.suscribir, name='suscribir'),
    # path('success', views.stripe_success, name='success'),
    # path('cancel', views.stripe_cancel, name='cancel'),

]

