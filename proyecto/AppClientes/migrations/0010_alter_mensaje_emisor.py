# Generated by Django 4.1.6 on 2023-05-06 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppClientes', '0009_alter_mensaje_emisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
