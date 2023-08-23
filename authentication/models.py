from tkinter import N
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from rest_framework.authtoken.models import Token
from authentication.validators import validate_isnumeric
from tournaments.models import Room
from authentication.fields import PasswordField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.mail.message import EmailMessage
from two_factor.models import get_available_methods
from two_factor.views import core

# Create your models here.


class User(AbstractUser):
    AbstractUser.first_name.max_length, AbstractUser.first_name.blank = (
        400, False)
    AbstractUser.username.max_length, AbstractUser.username.primary_key = (
        128, False)
    AbstractUser.last_name.max_length, AbstractUser.last_name.blank = (
        400, False)
    email = models.EmailField(
        max_length=256, blank=False, unique=True, primary_key=True)
    password = PasswordField()
    birth_date = models.DateField(default=date(2000, 1, 1))
    logged_in = models.BooleanField(default=False)
    security_pin = models.CharField(max_length=20, blank=False, null=True, default=None, validators=[
                                    validate_isnumeric], unique=True)
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT, related_name='members', null=True, blank=True, default=None)
    current_page = models.URLField(
        _('current_page'), default='authentication/')
    account_type = models.TextField(choices=[
        ('ST', 'Student'),
        ('TR', 'Teacher'),
        ('PT', 'Parent'),
        ('PL', 'Personal')
    ])
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'birth_date']

    def __str__(self):
        s = f"You are signed in as {self.email}"
        return s

    class Meta:
        db_table = "User"
        verbose_name = "user"
        verbose_name_plural = "users"

    def send_message(self, subject, body, from_email=None, to=None, cc=None, bcc=None, headers=None, path=''):
        if to == None:
            to = self.email
        email = EmailMessage(subject=subject, body=body,
                             from_email=from_email, to=to, cc=cc, bcc=bcc, headers=headers)
        if path:
            email.attach_file(path)
        email.message()
        email.send()


class TwoFactorChoice(models.Model):
    totp_enabled = models.BooleanField(default=False)
    sms_enabled = models.BooleanField(default=False)
    call_enabled = models.BooleanField(default=False)


# Signals


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save,sender=TwoFactorChoice)
def setup_two_factor_methods(sender,instance,**kwargs):
    user = instance.user
    if instance.totp_enabled:
        for method in get_available_methods():
            if method.name == 'totp':
                core.setup_view(TOTPDeviceConfigView.as_view(),user=user,redirect_url=None)
    if instance.sms_enabled:
        for method in get_available_methods():
            if method.name == 'sms':
                core.setup_view(SMSDeviceConfigView.as_view(),user=user,redirect_url=None)
    if instance.call_enabled:
        for method in get_available_methods():
            if method.name == 'call':
                core.setup_view(CallDeviceConfigView.as_view(),user=user,redirect_url=None)