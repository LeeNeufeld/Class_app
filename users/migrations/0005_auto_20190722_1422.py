# Generated by Django 2.2.2 on 2019-07-22 20:22

import django.core.validators
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190718_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), users.models.max_value_current_year], verbose_name='age'),
        ),
    ]
