from django.db import models
from datetime import date
from authentication.validators import validate_isnumeric
from tournaments.models import Room
from authentication.fields import DateField, PasswordField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
    super().first_name.max_length, super().first_name.blank = (400, False)
    super().username.max_length, super().username.primary_key = (128, True)
    super().last_name.max_length, super().last_name.blank = (400, False)
    super().email.max_length, super().email.blank, super().email.unique = (256, False, True)
    password = PasswordField()
    birth_date = DateField()
    logged_in = models.BooleanField(default=False)
    security_pin = models.CharField(max_length=20, blank=False, null=True, default=None, validators=[
                                    validate_isnumeric], unique=True)
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT, related_name='members', null=True, blank=True, default=None)
    current_page = models.URLField(
        _('current_page'), default='authentication/')

    def __str__(self):
        s = "You are signed in as {}"
        return s.format(self.user_email)

    class Meta:
        db_table = "User"
