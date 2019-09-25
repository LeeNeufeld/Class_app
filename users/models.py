from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import datetime


validate_caPostalCode = RegexValidator(
    regex=r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) *(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$', message="Please enter a valid Canadian Postal Code")
validate_usZipCode = RegexValidator(
    regex=r"^\d{5}([\-]?\d{4})?$", message="Please enter a valid US Zip Code")
validate_ukPostalCode = RegexValidator(
    regex=r"^(GIR|[A-Z]\d[A-Z\d]??|[A-Z]{2}\d[A-Z\d]??)[ ]??(\d[A-Z]{2})$", message="Please enter a valid UK Postal Code")
validate_auPostalCode = RegexValidator(
    regex=r"^(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})$", message="Please enter a valid Australia Postal Code")


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


gender_choices = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("NON-BINARY", "Non-Binary")
)

country_choices = (
    ("CANADA", "Canada"),
    ("USA", "USA"),
    ("UNITED KINGDOM", "United Kingdom"),
    ("AUSTRALIA", "Australia")
)
income_choices = (
    ("$0 - $34,999", "$0 - $34,999"),
    ("$35,000 - $49,999", "$35,000 - $49,999"),
    ("$50,000 - $69,999", "$50,000 - $69,999"),
    ("$70,000 - $99,999", "$70,000 - $99,999"),
    ("$100,000 - $149,999", "$100,000 - $149,999"),
    ("$150,000 - $249,999", "$150,000 - $249,999"),
    ("$250,000 or more", "$250,000 or more")
)
school_choices = (
    ("Some high school", "Some high school"),
    ("High school diploma or equivalent", "High school diploma or equivalent"),
    ("Trades certification", "Trades certification"),
    ("College diploma", "College diploma"),
    ("Bachelor’s degree", "Bachelor’s degree"),
    ("Graduate degree", "Graduate degree"),
    ("Professional degree", "Professional degree")
)


class CustomUser(AbstractUser):
    pass
    screen_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(('age'), validators=[
                              MinValueValidator(1900), max_value_current_year], null=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    country = models.CharField(max_length=50, choices=country_choices)
    postal_code = models.CharField(max_length=10)
    education_attainment = models.TextField(choices=school_choices, null=True)
    income = models.TextField(choices=income_choices, null=True)
    ethnicity = models.TextField(null=True)
    nationality = CountryField(blank_label='(select country)', null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.email
