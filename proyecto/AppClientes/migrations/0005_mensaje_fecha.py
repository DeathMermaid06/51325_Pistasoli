# Generated by Django 4.1.6 on 2023-05-06 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClientes', '0004_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
