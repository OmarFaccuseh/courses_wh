from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# Create your models here.
class Curso(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Tema(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    email_req = models.BooleanField(default=False)
    # imagen

    contenido = models.TextField(max_length=100000)





