# Generated by Django 5.0.2 on 2024-06-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0018_alter_pago_permiso'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(default='0000-0000', max_length=8),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fechapago',
            field=models.DateField(),
        ),
    ]
