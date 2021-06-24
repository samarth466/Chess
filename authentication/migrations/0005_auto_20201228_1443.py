# Generated by Django 3.1.3 on 2020-12-28 19:43

import django.contrib.auth.models
import django.contrib.auth.password_validation
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0014_auto_20201126_2338'),
        ('UserAuth', '0004_user_game'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_birth_date',
            new_name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_username',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=256, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=30, null=True, validators=[django.contrib.auth.password_validation.MinimumLengthValidator, django.contrib.auth.password_validation.UserAttributeSimilarityValidator, django.contrib.auth.password_validation.CommonPasswordValidator, django.contrib.auth.password_validation.NumericPasswordValidator]),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': 'A User with that user name already exists.'}, max_length=128, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]),
        ),
    ]
