from django.contrib import admin
from UserAuth.models import User
from django.contrib.auth.models import User as us

# Register your models here.
user_admin = admin.sites.AdminSite(name='User')
user_admin.register(model_or_iterable=User)