# Generated by Django 3.0.8 on 2020-07-25 16:47

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200725_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='userextended',
            name='about',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userextended',
            name='birthday',
            field=models.DateField(default=datetime.date(2020, 7, 25)),
        ),
    ]
