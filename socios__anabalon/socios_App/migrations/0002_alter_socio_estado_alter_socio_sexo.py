# Generated by Django 4.1 on 2022-11-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='socio',
            name='sexo',
            field=models.CharField(max_length=15),
        ),
    ]
