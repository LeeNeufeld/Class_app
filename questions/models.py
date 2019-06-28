from django.db import models

class Questions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question
