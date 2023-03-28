from django.db import models
# Create your models here.

from django.db import models

class User (models.Model):
    user = models.CharField(max_length=20)
    name_user = models.CharField(max_length=85)
    password= models.CharField(max_length=20)
    email = models.CharField(max_length=40)