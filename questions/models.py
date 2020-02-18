from django.db import models
# Model for the questions table in DB


class Questions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question
