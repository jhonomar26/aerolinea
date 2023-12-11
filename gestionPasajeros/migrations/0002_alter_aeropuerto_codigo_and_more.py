# Generated by Django 4.2.7 on 2023-12-07 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPasajeros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeropuerto',
            name='codigo',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='codigo_pasajero',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='num_vuelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_pasajeros', to='gestionPasajeros.vuelo'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='cod_aeropuerto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_vuelos', to='gestionPasajeros.aeropuerto'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='numero_vuelo',
            field=models.IntegerField(unique=True),
        ),
    ]
