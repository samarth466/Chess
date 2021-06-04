from django.contrib import admin
from UserAuth.models import User

# Register your models here.
user_admin = admin.sites.AdminSite(name='User')
user_admin.register(model_or_iterable=User)