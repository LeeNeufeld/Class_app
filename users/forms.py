# users/forms.py
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import datetime


def current_year():
    return datetime.date.today().year


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year+1)]


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
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    age = forms.ChoiceField(choices=year_choices,
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
    ethnicity = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input-field col s12'
        }
    ))

    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'age',
                  'gender',
                  'country',
                  'education_attainment',
                  'income',
                  'ethnicity',
                  'nationality',
                  'postal_code',
                  'password')
