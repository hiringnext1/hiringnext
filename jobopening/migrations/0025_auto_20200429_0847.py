# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-29 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0024_auto_20190319_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobopening',
            name='default_industry',
        ),
        migrations.RemoveField(
            model_name='jobopening',
            name='experience_choice',
        ),
        migrations.RemoveField(
            model_name='jobopening',
            name='functional_area',
        ),
        migrations.RemoveField(
            model_name='jobopening',
            name='job_location_sample',
        ),
        migrations.RemoveField(
            model_name='jobopening',
            name='nice_to_have',
        ),
        migrations.RemoveField(
            model_name='jobopening',
            name='role_category',
        ),
    ]
