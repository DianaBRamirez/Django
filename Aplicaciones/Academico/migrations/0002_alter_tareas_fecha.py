# Generated by Django 4.1.7 on 2024-01-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
