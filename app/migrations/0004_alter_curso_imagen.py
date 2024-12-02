# Generated by Django 5.1.2 on 2024-10-23 02:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_curso_descripcion_curso_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]