from django.db import models
from django.db.models.signals import pre_save, pre_delete
import os
import pathlib
from django.conf import settings
import random
import string

# Create your models here.
