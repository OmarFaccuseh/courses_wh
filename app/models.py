from django.db import models
from django.contrib.auth.models import User
import helpers
from cloudinary.models import CloudinaryField
helpers.cloudinary_init()
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

# # #  Utilities  # # #

def get_display_name_image(instance):
    if isinstance(instance, Curso):
        return f'{instance.name} - course'
    elif isinstance(instance, Tema):
        return f'{instance.name} > {instance.curso.name } - course'
    else:
        return 'Generic name'


def get_image_build(instance, field_name='imagen', as_html=False, width=1200):
    if not hasattr(instance, field_name):
        return ""
    image_object = getattr(instance, field_name)
    if not image_object:
        return ""
    image_options = {"width": width}
    if as_html:
        return image_object.image(**image_options)
    url = image_object.build_url(**image_options)
    return url


# # #  Choises  # # #  

class Calificacion(models.TextChoices):
    CERO = 'cero', 'Cero'
    UNO = 'uno', 'Uno'
    DOS = 'dos', 'Dos'
    TRES = 'tres', 'Tres'
    CUATRO = 'cuatro', 'Cuatro'
    CINCO = 'cinco', 'Cinco'

class Tipo(models.TextChoices):
    SNACK = 'snack', 'Snack'
    CURSO = 'curso', 'Curso'

class Categoria(models.TextChoices):
    BACKEND = 'backend', 'Backend'
    FRONTEND = 'frontend', 'Frontend'

# # #  Models  # # #

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField('Curso', related_name='alumnos')


class Nota(models.Model):
    perfil = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notas')  
    contenido = models.TextField()  
    fecha_creacion = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Nota de {self.perfil.user.username}: {self.contenido[:20]}..."  # Muestra un resumen de la nota


class Curso(models.Model):
    name = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=500, default='')
    imagen = CloudinaryField('image', null=True, blank=True, display_name=get_display_name_image)
    tags = models.CharField(max_length=250, null=True, blank=True)
    categoria = models.CharField(choices=Categoria.choices, default=Categoria.BACKEND)
    tipo = models.CharField(choices=Tipo.choices, default=Tipo.CURSO)
    calificacion = models.CharField(choices=Calificacion.choices, default=Calificacion.CERO)

    @property
    def cant_temas(self):
        return self.tema_set.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('curso', args=[self.id])

    def get_image_build_course_sm(self):
        return get_image_build(self, width=350)

    def get_image_build_course_md(self):
        return get_image_build(self, width=700)

    def get_tags(self):
        return self.tags.split(',') if self.tags else []


class Tema(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False, blank=False)
    email_req = models.BooleanField(default=False)
    imagen = CloudinaryField('image', null=True, display_name=get_display_name_image)
    contenido = models.TextField(max_length=100000)

    def get_absolute_url(self):
        return reverse('tema', args=[self.id])


# # #  Signals  # # #
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()



