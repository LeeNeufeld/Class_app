# Generated by Django 2.2.2 on 2019-09-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0011_auto_20190919_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totals',
            name='userId',
            field=models.IntegerField(null=True),
        ),
    ]
