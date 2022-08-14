from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",
                  "password1", "password2",
                  "first_name",
                  "last_name", "tel", "photo", "role")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",
                  "password",
                  "first_name",
                  "last_name", "tel", "photo", "role", "subrole")
