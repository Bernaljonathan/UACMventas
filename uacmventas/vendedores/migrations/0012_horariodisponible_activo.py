# Generated by Django 4.1.3 on 2023-09-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0011_vendedor_activo_vendedor_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='horariodisponible',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
