# Generated by Django 5.0.2 on 2024-06-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0020_remove_pago_permiso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='nombre_area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nombre_cargo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nombre_departamento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='carnet',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='dui',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombres',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(default='0000-0000', max_length=8),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre_municipio',
            field=models.CharField(max_length=50),
        ),
    ]
