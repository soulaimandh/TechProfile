from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, verbose_name="Date de naissance")
    address = models.TextField(null=True, verbose_name="Adresse")
    phone_number = models.CharField(max_length=255, null=True, verbose_name="Numéro de téléphone")

    def __str__(self):
        return self.username
