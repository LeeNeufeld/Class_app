from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from questions.models import Questions
from sentences.models import ClassSentence


validate_caPostalCode = RegexValidator(
    regex=r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) *(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$', message="Please enter a valid Canadian Postal Code")
validate_usZipCode = RegexValidator(
    regex=r"^\d{5}([\-]?\d{4})?$", message="Please enter a valid US Zip Code")
validate_ukPostalCode = RegexValidator(
    regex=r"^(GIR|[A-Z]\d[A-Z\d]??|[A-Z]{2}\d[A-Z\d]??)[ ]??(\d[A-Z]{2})$", message="Please enter a valid UK Postal Code")
validate_auPostalCode = RegexValidator(
    regex=r"^(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})$", message="Please enter a valid Australia Postal Code")


class CareResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class FairResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class LoyResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class AuthResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class SanResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class LibResponses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.CharField(max_length=15, null=True)
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, null=True)


class Totals(models.Model):
    userid = models.IntegerField(null=True)
    screen_name = models.CharField(max_length=100, null=True)
    total = models.IntegerField(null=True)
    care_harm = models.IntegerField(null=True)
    care_harm_yes = models.IntegerField(null=True)
    care_harm_no = models.IntegerField(null=True)
    fairness_cheating = models.IntegerField(null=True)
    fairness_cheating_yes = models.IntegerField(null=True)
    fairness_cheating_no = models.IntegerField(null=True)
    loyalty_betrayal = models.IntegerField(null=True)
    loyalty_betrayal_yes = models.IntegerField(null=True)
    loyalty_betrayal_no = models.IntegerField(null=True)
    authority_subversion = models.IntegerField(null=True)
    authority_subversion_yes = models.IntegerField(null=True)
    authority_subversion_no = models.IntegerField(null=True)
    sanctity_degradation = models.IntegerField(null=True)
    sanctity_degradation_yes = models.IntegerField(null=True)
    sanctity_degradation_no = models.IntegerField(null=True)
    liberty_oppression = models.IntegerField(null=True)
    liberty_oppression_yes = models.IntegerField(null=True)
    liberty_oppression_no = models.IntegerField(null=True)
