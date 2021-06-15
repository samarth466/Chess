from django.db import models
from datetime import date, datetime
from django.utils import timezone as tz
from django import forms
from django.contrib.auth.password_validation import (
    MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator
)
from django.db.backends.base.base import BaseDatabaseWrapper


class DateField(models.Field):

    def __init__(self, date=None, default=date(tz.now().year, 1, 1), *args, **kwargs):
        self.date = date
        if self.date == None:
            self.date = kwargs['default'] = default
        else:
            kwargs['date'] = self.date
        kwargs['unique'] = False
        kwargs['blank'] = False
        kwargs['null'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.date != None:
            kwargs['date'] = self.date
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        value = self.date
        setattr(model_instance, self.attname, value)
        return value

    def db_type(self, connection):
        return 'Date'

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.DateField}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class PasswordField(models.CharField):

    def __init__(self, max_length=30, min_length=5, *args, **kwargs):
        kwargs['null'] = False
        kwargs['max_length'] = max_length
        kwargs['min_length'] = min_length
        kwargs['blank'] = False
        kwargs['validators'] = [MinimumLengthValidator, UserAttributeSimilarityValidator,
                                CommonPasswordValidator, NumericPasswordValidator]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'Password'
