# Generated by Django 4.1.3 on 2023-07-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='titulo',
            field=models.CharField(default='Tu producto', max_length=200),
        ),
    ]
