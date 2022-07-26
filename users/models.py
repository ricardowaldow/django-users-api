from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
class User(models.Model):
    nome = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = EncryptedCharField(max_length=30, blank=False, null=False)