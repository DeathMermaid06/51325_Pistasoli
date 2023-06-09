# Generated by Django 4.1.6 on 2023-05-05 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClientes', '0002_pedido_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='razonsocial',
            new_name='cliente',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='factura',
            name='peso',
            field=models.IntegerField(),
        ),
    ]
