# Generated by Django 3.1.3 on 2020-12-29 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0005_auto_20201228_2200'),
        ('settings', '0003_auto_20201228_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='UserAuth.user'),
        ),
    ]
