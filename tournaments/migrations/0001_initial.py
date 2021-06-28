# Generated by Django 3.2.4 on 2021-06-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]