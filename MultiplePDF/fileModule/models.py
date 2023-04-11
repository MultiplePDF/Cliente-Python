from django.db import models

# Create your models here.
from django.db import models

class File(models.Model):
    fileName = models.CharField(max_length=100)
    serializedFile = models.TextField()
