# Generated by Django 5.1.2 on 2024-11-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('idSucursales', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=30)),
                ('gerente', models.CharField(max_length=50)),
                ('horarioAtencion', models.CharField(max_length=20)),
            ],
        ),
    ]
