import email
from statistics import mode
from django.db import models
class User(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)