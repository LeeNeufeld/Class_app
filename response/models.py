from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from questions.models import Questions
from sentences.models import ClassSentence

class Responses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.BooleanField(default=True)
    userId = models.IntegerField(null=True)


