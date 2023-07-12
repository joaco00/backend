# Generated by Django 4.1 on 2022-11-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios_App', '0002_alter_socio_estado_alter_socio_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Vigente'), (2, 'Suspendido'), (3, 'Retirado')], default=1),
        ),
        migrations.AlterField(
            model_name='socio',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')], default=1),
        ),
    ]