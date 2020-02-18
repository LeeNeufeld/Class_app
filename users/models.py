from django.db import models  # imports built django forms
# imports country field from the countries dependancy
from django_countries.fields import CountryField
# imports abstract user function to create custom user information
from django.contrib.auth.models import AbstractUser
# imports validators for the regexs
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import datetime

# postal code regex
validate_caPostalCode = RegexValidator(
    regex=r'^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ]) *(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$', message="Please enter a valid Canadian Postal Code")
# zip code regex
validate_usZipCode = RegexValidator(
    regex=r"^\d{5}([\-]?\d{4})?$", message="Please enter a valid US Zip Code")
# UK Postal code regex
validate_ukPostalCode = RegexValidator(
    regex=r"^(GIR|[A-Z]\d[A-Z\d]??|[A-Z]{2}\d[A-Z\d]??)[ ]??(\d[A-Z]{2})$", message="Please enter a valid UK Postal Code")
# australia postal code regex
validate_auPostalCode = RegexValidator(
    regex=r"^(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})$", message="Please enter a valid Australia Postal Code")

# function to calculate current year to use in year of birth field


def current_year():
    return datetime.date.today().year

# function to validate the current year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


# define choices for gender field
gender_choices = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("NON-BINARY", "Non-Binary")
)
# define choices for country field
country_choices = (
    ("CANADA", "Canada"),
    ("USA", "USA"),
    ("UNITED KINGDOM", "United Kingdom"),
    ("AUSTRALIA", "Australia")
)
# define choices for income field
income_choices = (
    ("$0 - $34,999", "$0 - $34,999"),
    ("$35,000 - $49,999", "$35,000 - $49,999"),
    ("$50,000 - $69,999", "$50,000 - $69,999"),
    ("$70,000 - $99,999", "$70,000 - $99,999"),
    ("$100,000 - $149,999", "$100,000 - $149,999"),
    ("$150,000 - $249,999", "$150,000 - $249,999"),
    ("$250,000 or more", "$250,000 or more")
)
# define choices for education field
school_choices = (
    ("No high school diploma or equivalent",
     "No high school diploma or equivalent"),
    ("High school (secondary school) diploma or equivalent",
     "High school (secondary school) diploma or equivalent"),
    ("Certificate of Apprenticeship or Certificate of Qualification or other trades certificate or diploma",
     "Certificate of Apprenticeship or Certificate of Qualification or other trades certificate or diploma"),
    ("College, CEGEP or other non-university certificate or diploma",
     "College, CEGEP or other non-university certificate or diploma"),
    ("University certificate, diploma or degree at the bachelor level or below",
     "University certificate, diploma or degree at the bachelor level or below"),
    ("Degree in medicine, dentistry, veterinary medicine or optometry (M.D., D.D.S., D.M.D., D.V.M., O.D.), master's degree (e.g., M.A., M.Sc., M.Ed., M.B.A.) or earned doctorate (e.g., Ph.D.)",
     "Degree in medicine, dentistry, veterinary medicine or optometry (M.D., D.D.S., D.M.D., D.V.M., O.D.), master's degree (e.g., M.A., M.Sc., M.Ed., M.B.A.) or earned doctorate (e.g., Ph.D.)")
)
# define choices for urbanization field
urban_choices = (
    ("Large urban centre (population 100,000 or more)",
     "Large urban centre (population 100,000 or more)"),
    ("Medium population centres (population 30,000 to 99,999)",
     "Medium population centres (population 30,000 to 99,999)"),
    ("Small population centres (population 1,000 to 29,999)",
     "Small population centres (population 1,000 to 29,999)"),
    ("Rural Area", "Rural Area")
)
# define choices for ethnicity field
ethnic_choices = (
    ('White', 'White'),
    ('South Asian (e.g., East Indian, Pakistani, Sri Lankan, etc.)',
     'South Asian (e.g., East Indian, Pakistani, Sri Lankan, etc.)'),
    ('Chinese', 'Chinese'),
    ('Black', 'Black'),
    ('Filipino', 'Filipino'),
    ('Latin American', 'Latin American'),
    ('Arab', 'Arab'),
    ('Southeast Asian (e.g., Vietnamese, Cambodian, Laotian, Thai, etc.)',
     'Southeast Asian (e.g., Vietnamese, Cambodian, Laotian, Thai, etc.)'),
    ('West Asian (e.g., Iranian, Afghan, etc.)',
     'West Asian (e.g., Iranian, Afghan, etc.)'),
    ('Korean', 'Korean'),
    ('Japanese', 'Japanese'),
    ('Other', 'Other'),
    ('', '')
)
# define choices for religion field
religion_choices = (
    ('Buddhist', 'Buddhist'),
    ('Christian', (
        ('Anglican', 'Anglican'),
        ('Baptist', 'Baptist'),
        ('Catholic', 'Catholic'),
        ('Christian Orthodox', 'Christian Orthodox'),
        ('Lutheran', 'Lutheran'),
        ('Pentecostal', 'Pentecostal'),
        ('Presbyterian', 'Presbyterian'),
        ('United Church', 'United Church'),
        ('Other Christian', 'Other Christian'),
    )),
    ('Hindu', 'Hindu'),
    ('Jewish', 'Jewish'),
    ('Muslim', 'Muslim'),
    ('Sikh', 'Sikh'),
    ('Traditional (Aboriginal) Spirituality',
     'Traditional (Aboriginal) Spirituality'),
    ('Other religions', 'Other religions'),
    ('No religious affiliation', 'No religious affiliation'),
)

# creates the custom user model that includes the built in django fields as well as our own custom fields


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
    ethnicity = models.TextField(choices=ethnic_choices, null=True)
    nationality = CountryField(blank_label='(select country)', null=True)
    urbanization = models.TextField(choices=urban_choices, null=True)
    religion = models.TextField(choices=religion_choices, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.email
