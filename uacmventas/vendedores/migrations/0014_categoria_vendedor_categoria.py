# Generated by Django 4.1.3 on 2023-10-08 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0013_rename_activo_horariodisponible_horario_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='vendedor',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='vendedores.categoria'),
        ),
    ]
