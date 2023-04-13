from django.db import models
from authentication.models import User

# Create your models here.


class GoogleTokens(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='tokens', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expiry = models.DateTimeField()
    token_type = models.CharField(max_length=50)

    class Meta:
        db_table = "Google_Tokens"
        verbose_name = "google tokens"
        verbose_name_plural = "google tokens"