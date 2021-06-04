from django.db import models
from datetime import date, datetime
from django import forms


class DateField(models.Field):

    def __init__(self, date=None, default=date(date.today().year, 1, 1), *args, **kwargs):
        self.date = date
        if self.date == None:
            self.date = kwargs['default'] = datetime(
                default.year, default.month, default.day)
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

# class ForeignKey(models.ForeignKey)
