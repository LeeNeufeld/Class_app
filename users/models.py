from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
     
    def __str__(self):
        return self.email

