# Generated by Django 4.1.6 on 2023-05-05 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMain', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='Sabores',
        ),
    ]