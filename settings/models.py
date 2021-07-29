from django.db import models
from authentication.models import User

# Create your models here.


class Settings(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='settings', null=False, primary_key=True)
    voice_assistant = models.BooleanField(default=True)

    def __str__(self):
        return "{}'s settings".format(self.user.user_username)

    class Meta:
        db_table = "Settings"
