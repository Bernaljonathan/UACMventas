# Generated by Django 4.1.3 on 2023-08-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0003_vendedor_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='imagen',
            field=models.ImageField(upload_to='vendedores/'),
        ),
    ]
