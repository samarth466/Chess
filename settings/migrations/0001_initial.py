# Generated by Django 3.2.4 on 2021-07-21 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='settings', serialize=False, to='authentication.user')),
                ('voice_assistant', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Settings',
            },
        ),
    ]
