from django.db import models


class ClassSentence(models.Model):
    id = models.FloatField(blank=True, primary_key=True)
    sentence = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_sentence'
