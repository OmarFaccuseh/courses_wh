# Generated by Django 5.1.2 on 2024-10-27 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_tema_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tema',
            old_name='nombre',
            new_name='name',
        ),
    ]