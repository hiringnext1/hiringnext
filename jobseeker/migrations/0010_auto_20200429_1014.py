# Generated by Django 3.0.5 on 2020-04-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0009_auto_20181226_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='feedback_update',
            field=models.CharField(choices=[('Resume Submitted', 'Resume Submitted'), ('profile shared', 'profile shared'), ('Shortlisted', 'Shortlisted'), ('Screening Rejected', 'Screening Rejected'), ('Interview Attended', 'Interview Attended'), ('Interview not attended', 'Interview not attended'), ('Selected', 'Selected'), ('Rejected', 'Rejected'), ('Salary Offered', 'Salary Offered'), ('Offered Accepted', 'Offered Accepted'), ('Offer rejected', 'Offer rejected'), ('Submit Documents', 'Submit Documents'), ('Joined', 'Joined')], max_length=200),
        ),
    ]
