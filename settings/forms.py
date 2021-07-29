from django.db import models
from django.forms import ModelForm
from rest_framework import fields
from .models import Settings

# Create the form class.

class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        fields = ['user']