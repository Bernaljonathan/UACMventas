# Generated by Django 4.1.3 on 2023-09-02 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0009_alter_articulo_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='comentario',
            field=models.TextField(null=True),
        ),
    ]
