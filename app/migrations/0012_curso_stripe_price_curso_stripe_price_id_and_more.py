# Generated by Django 5.1.3 on 2024-12-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='stripe_price',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='curso',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
