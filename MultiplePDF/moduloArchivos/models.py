from django.db import models

# Create your models here.
from django.db import models

class Archivo(models.Model):
    nombre = models.CharField(max_length=100)
    archivo_serializado = models.TextField()
