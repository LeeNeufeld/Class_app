# Generated by Django 2.2.2 on 2019-07-22 18:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0004_responses_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='responses',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='responses',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='responses',
            name='postal_code',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Please enter a valid Canadian Postal Code', regex='^([ABCEGHJKLMNPRSTVXY]\\d[ABCEGHJKLMNPRSTVWXYZ]) *(\\d[ABCEGHJKLMNPRSTVWXYZ]\\d)$'), django.core.validators.RegexValidator(message='Please enter a valid Australia Postal Code', regex='^(0[289][0-9]{2})|([1345689][0-9]{3})|(2[0-8][0-9]{2})|(290[0-9])|(291[0-4])|(7[0-4][0-9]{2})|(7[8-9][0-9]{2})$'), django.core.validators.RegexValidator(message='Please enter a valid US Zip Code', regex='^\\d{5}([\\-]?\\d{4})?$'), django.core.validators.RegexValidator(message='Please enter a valid UK Postal Code', regex='^(GIR|[A-Z]\\d[A-Z\\d]??|[A-Z]{2}\\d[A-Z\\d]??)[ ]??(\\d[A-Z]{2})$')]),
        ),
    ]