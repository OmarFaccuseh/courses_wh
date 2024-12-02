# Generated by Django 5.1.2 on 2024-10-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/'),
        ),
    ]