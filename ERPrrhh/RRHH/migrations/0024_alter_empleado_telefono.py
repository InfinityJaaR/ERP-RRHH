# Generated by Django 5.0.2 on 2024-06-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0023_alter_empleado_dui'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(default='0000-0000', max_length=9),
        ),
    ]
