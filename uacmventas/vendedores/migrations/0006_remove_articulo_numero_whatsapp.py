# Generated by Django 4.1.3 on 2023-08-05 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0005_articulo_numero_whatsapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='numero_whatsapp',
        ),
    ]
