# users/forms.py
from django import forms  # imports built django forms
# imports country field from the countries dependancy
from django_countries.fields import CountryField
# imports country selct widget from countries dependancy
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User  # imports the user model
# imports user creation and change forms from Django
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser  # imports the custom user model
import datetime  # imports Django datetime function

# defines the current year using the datetime function to use in the date of birth field


def current_year():
    return datetime.date.today().year

# provides a list of years that start at 1900 and extend to the current year to display in the date of birth field


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year+1)]


# defines the choices for the gender field
gender_choices = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("NON-BINARY", "Non-Binary")
)
# defines choices for the country field
country_choices = (
    ("CANADA", "Canada"),
    ("USA", "USA"),
    ("UNITED KINGDOM", "United Kingdom"),
    ("AUSTRALIA", "Australia")
)
# defines choices for the income field
income_choices = (
    ("$0 - $34,999", "$0 - $34,999"),
    ("$35,000 - $49,999", "$35,000 - $49,999"),
    ("$50,000 - $69,999", "$50,000 - $69,999"),
    ("$70,000 - $99,999", "$70,000 - $99,999"),
    ("$100,000 - $149,999", "$100,000 - $149,999"),
    ("$150,000 - $249,999", "$150,000 - $249,999"),
    ("$250,000 or more", "$250,000 or more")
)
# defines choices for the educational atainment field
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
# defines choices for the urbanization field
urban_choices = (
    ("Large urban centre (population 100,000 or more)",
     "Large urban centre (population 100,000 or more)"),
    ("Medium population centres (population 30,000 to 99,999)",
     "Medium population centres (population 30,000 to 99,999)"),
    ("Small population centres (population 1,000 to 29,999)",
     "Small population centres (population 1,000 to 29,999)"),
    ("Rural Area", "Rural Area")
)
# defines choices for the ethnicity field
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
)
# defines choices for the religion field
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

# built in form to creat a new user. not used


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'first_name',
                  'last_name',
                  'age',
                  'gender',
                  'postal_code',
                  'country')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        if commit:
            user.save()  # saves the user info if form is used
        return user

# custom user change form that is used in the edit profile page. all styling is done here within the form.


class CustomUserChangeForm(UserChangeForm):
    age = forms.ChoiceField(choices=year_choices,
                            widget=forms.Select(
                                attrs={
                                    'class': 'input-field col s12'

                                }
                            ))
    religion = forms.ChoiceField(choices=religion_choices,
                                 widget=forms.Select(
                                     attrs={
                                         'class': 'input-field col s12'

                                     }
                                 ))
    gender = forms.ChoiceField(choices=gender_choices,
                               widget=forms.Select(
                                   attrs={
                                       'class': 'input-field col s12'
                                   }
                               ))
    urbanization = forms.ChoiceField(choices=urban_choices,
                                     widget=forms.Select(
                                         attrs={
                                             'class': 'input-field col s12'
                                         }
                                     ))
    country = forms.ChoiceField(choices=country_choices,
                                widget=forms.Select(
                                    attrs={
                                        'class': 'input-field col s12'
                                    }
                                ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    screen_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    postal_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    nationality = CountryField().formfield(
        widget=CountrySelectWidget(
            attrs={"class": "input-field col s12"}
        )
    )
    income = forms.ChoiceField(choices=income_choices, widget=forms.Select(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    education_attainment = forms.ChoiceField(choices=school_choices, widget=forms.Select(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    ethnicity = forms.ChoiceField(choices=ethnic_choices, widget=forms.Select(
        attrs={
            'class': 'input-field col s12'
        }
    ))
    password = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'screen_name',
                  'first_name',
                  'last_name',
                  'age',
                  'gender',
                  'country',
                  'education_attainment',
                  'income',
                  'urbanization',
                  'ethnicity',
                  'nationality',
                  'postal_code',
                  'password')
