# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-29 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobopening', '0027_auto_20200429_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopening',
            name='skill',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Skills'),
        ),
    ]
