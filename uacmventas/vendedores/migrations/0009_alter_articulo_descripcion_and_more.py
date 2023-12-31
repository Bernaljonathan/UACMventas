# Generated by Django 4.1.3 on 2023-08-13 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0008_vendedor_numero_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='numero_whatsapp',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='HorarioDisponible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedores.vendedor')),
            ],
        ),
    ]
