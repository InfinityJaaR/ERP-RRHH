# Generated by Django 5.0.2 on 2024-05-31 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='horas_extras_nocturnas',
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='horas_extras_diurnas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='horas_trabajadas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='mes_asistencia',
            field=models.CharField(choices=[('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'), ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'), ('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'), ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')],default='1',max_length=2),
        ),
    ]
