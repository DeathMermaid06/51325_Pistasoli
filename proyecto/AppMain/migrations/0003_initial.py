# Generated by Django 4.1.6 on 2023-05-06 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppMain', '0002_delete_cliente_delete_factura_delete_pedido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotosblog')),
            ],
        ),
    ]
