from django.db import models
from datetime import date, datetime
from django.utils import timezone as tz
from django import forms
from django.contrib.auth.password_validation import (
    MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator
)
from django.db.backends.base.base import BaseDatabaseWrapper


class PasswordField(models.CharField):

    def __init__(self, max_length=30, min_length=5, *args, **kwargs):
        kwargs['null'] = False
        kwargs['max_length'] = max_length
        kwargs['blank'] = False
        kwargs['validators'] = [MinimumLengthValidator, UserAttributeSimilarityValidator,
                                CommonPasswordValidator, NumericPasswordValidator]
        super().__init__(*args, **kwargs)
        kwargs['min_length'] = min_length

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'Password'
