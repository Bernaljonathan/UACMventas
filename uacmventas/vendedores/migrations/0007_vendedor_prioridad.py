# Generated by Django 4.1.3 on 2023-08-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0006_remove_articulo_numero_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='prioridad',
            field=models.IntegerField(default=0),
        ),
    ]
