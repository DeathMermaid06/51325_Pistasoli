from django.db import models
import datetime

# Create your models here.

class ModelBlog(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=100)
    cuerpo=models.TextField()
    autor=models.CharField(max_length=50)
    fecha = models.DateField(default=datetime.date.today)
    imagen =models.ImageField(upload_to="fotosblog", null=True, blank=True)