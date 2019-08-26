from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from questions.models import Questions
from sentences.models import ClassSentence


validate_caPostalCode = RegexValidator(regex=r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) *(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$', message="Please enter a valid Canadian Postal Code")
validate_usZipCode = RegexValidator(regex=r"^\d{5}([\-]?\d{4})?$", message="Please enter a valid US Zip Code")
validate_ukPostalCode = RegexValidator(regex=r"^(GIR|[A-Z]\d[A-Z\d]??|[A-Z]{2}\d[A-Z\d]??)[ ]??(\d[A-Z]{2})$", message="Please enter a valid UK Postal Code")
validate_auPostalCode = RegexValidator(regex=r"^(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})$", message="Please enter a valid Australia Postal Code")

class Responses(models.Model):
    question = models.TextField()
    sentence = models.TextField()
    response = models.BooleanField(default=True)
    userId = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=10, validators=[validate_caPostalCode, validate_auPostalCode, validate_usZipCode, validate_ukPostalCode], null=True)


