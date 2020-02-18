# users/admin.py
from django.contrib import admin  # imports Django admin functions
from django.contrib.auth import get_user_model  # imports the user model
from django.contrib.auth.admin import UserAdmin  # imorts user admin funtions

# imports user forms from the forms.py file
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser  # imports the custom user model


# creates user admin model to allow login perams to change username to email
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
