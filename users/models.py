""" Users App Models """
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, encrypt_str
class User(models.Model):
    """User entity"""
    nome = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = EncryptedCharField(max_length=30, blank=False, null=False)

    def authenticate(self, client_email : str, client_password : str):
        """
        Authenticate user email and login.

        Returns a token if the data is correct
        """
        if self.email == client_email and self.password == client_password:
            token = encrypt_str(client_email).decode('utf-8')
            return {'token' : token }
        else:
            return {'message' : 'Incorrect email or password'}