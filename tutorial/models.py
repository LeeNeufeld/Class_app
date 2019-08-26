from django.db import models

class Tutorial(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.BooleanField()
