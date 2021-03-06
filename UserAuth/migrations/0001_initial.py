# Generated by Django 3.0.7 on 2020-08-08 21:44

import UserAuth.models
import UserAuth.validators
import datetime
import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=400)),
                ('user_username', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=256, unique=True)),
                ('user_password', models.CharField(max_length=30, validators=[django.contrib.auth.password_validation.MinimumLengthValidator, django.contrib.auth.password_validation.UserAttributeSimilarityValidator, django.contrib.auth.password_validation.CommonPasswordValidator, django.contrib.auth.password_validation.NumericPasswordValidator])),
                ('user_birth_date', UserAuth.models.DateField(date=datetime.datetime(2020, 1, 1, 0, 0), null=True)),
                ('logged_in', models.BooleanField(default=False)),
                ('security_pin', models.TextField(default=None, null=True, validators=[UserAuth.validators.validate_isnumeric])),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
