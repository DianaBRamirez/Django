# Generated by Django 4.1.7 on 2024-01-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0002_alter_tareas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='txtAct',
            field=models.CharField(max_length=100),
        ),
    ]