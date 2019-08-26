# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import datetime

def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]

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
            'class':'form-control'
        }
    ))
    gender = forms.ChoiceField(choices=gender_choices,
    widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    country = forms.ChoiceField(choices=country_choices,
    widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    postal_code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control'
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
                  'postal_code',
                  'password')

  