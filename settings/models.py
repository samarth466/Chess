from django.db import models
from authentication.models import User

# Create your models here.


class Settings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='settings', null=False, primary_key=True)
    dark_color_value = models.CharField(
        max_length=500, unique=False, blank=True, null=True, default='Black')
    light_color_value = models.CharField(
        max_length=500, unique=False, blank=True, null=True, default='White')
    voice_assistant = models.BooleanField(default=True)
    use_numpad_keys_for_movement = models.BooleanField(
        default=True, verbose_name="use numpad keys for movement of pieces")

    def __str__(self):
        return "{}'s settings".format(self.user.user_username)

    class Meta:
        db_table = "Settings"
