# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-04 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_auto_20181204_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='company_review',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
