from django.db import models
from django.conf import settings
from datetime import date, datetime
from django import forms
from django.apps import apps
from importlib import import_module


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

class PasswordField(models.CharField):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.max_length = kwargs['max_length'] = 50
        self.null = kwargs['null'] = False
        self.blank = kwargs['blank'] = False
    
    def __hash__(self):
        for app in settings.INSTALLED_APPS:
            if app.startswith('django.'):
                continue
            app_name = app.split('.')[0]
            app_models = apps.get_app_config(app_name).get_models()
            for model in app_models:
                for field in model._meta.get_fields():
                    if