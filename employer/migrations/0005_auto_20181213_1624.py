# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_auto_20181204_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='company_location',
            field=models.CharField(choices=[('Ahmadabad', 'Ahmadabad'), ('Vadodara', 'Vadodara'), ('Surat', 'Surat'), ('Rajkot', 'Rajkot'), ('Bharuch', 'Bharuch'), ('Ankleshwar', 'Ankleshwar'), ('Vapi', 'Vapi'), ('Valsad', 'Valsad'), ('Anand', 'Anand'), ('Mehsana', 'Mehsana'), ('Bhavnagar', 'Bhavnagar'), ('Junagadh', 'Junagadh'), ('Jamnagar', 'Jamnagar')], max_length=50),
        ),
        migrations.AlterField(
            model_name='referclient',
            name='location',
            field=models.CharField(choices=[('Ahmadabad', 'Ahmadabad'), ('Vadodara', 'Vadodara'), ('Surat', 'Surat'), ('Rajkot', 'Rajkot'), ('Bharuch', 'Bharuch'), ('Ankleshwar', 'Ankleshwar'), ('Vapi', 'Vapi'), ('Valsad', 'Valsad'), ('Anand', 'Anand'), ('Mehsana', 'Mehsana'), ('Bhavnagar', 'Bhavnagar'), ('Junagadh', 'Junagadh'), ('Jamnagar', 'Jamnagar')], max_length=50),
        ),
    ]
