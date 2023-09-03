# Generated by Django 4.1.3 on 2023-09-03 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0010_vendedor_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='email',
            field=models.EmailField(default='sample@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='comentario',
            field=models.TextField(blank=True),
        ),
    ]
