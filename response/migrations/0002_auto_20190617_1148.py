# Generated by Django 2.2.2 on 2019-06-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='question',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='responses',
            name='sentence',
            field=models.TextField(),
        ),
    ]