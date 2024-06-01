# Generated by Django 5.0.2 on 2024-05-31 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0012_alter_municipio_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='RRHH.departamento'),
        ),
    ]