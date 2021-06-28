from django.db import models
from datetime import date as Date, datetime
from django import forms
from UserAuth.validators import validate_isnumeric
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator
from tournaments.models import Room
from UserAuth.fields import DateField
from game.models import Game
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    first_name = models.CharField(max_length=200, default=None, null=True)
    username = models.CharField(max_length=128, unique=True, validators=[username_validator], error_messages={
                                'unique': _('A User with that user name already exists.')}, default=None, null=True)
    last_name = models.CharField(max_length=200, default=None, null=True)
    email = models.EmailField(
        max_length=256, unique=True, primary_key=True, default='')
    password = models.CharField(max_length=30, validators=[
                                MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator], default=None, null=True)
    birth_date = DateField(default=Date(datetime.now().year, 1, 1))
    logged_in = models.BooleanField(default=False)
    security_pin = models.CharField(max_length=20, blank=False, null=True, default=None, validators=[
                                    validate_isnumeric], unique=True)
    room = models.ForeignKey(
        Room, on_delete = models.PROTECT, related_name = 'members', null = True, blank = True, default = None)
    game = models.ForeignKey(
        Game, on_delete=models.SET_NULL, related_name='members', null=True)

    REQUIRED_FIELDS = ['email', 'first_name',
                       'last_name', 'password']

    def __str__(self):
        s = "You are signed in as {}"
        return s.format(self.user_email)

    class Meta:
        db_table = "User"
