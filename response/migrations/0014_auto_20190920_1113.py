# Generated by Django 2.2.2 on 2019-09-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0013_auto_20190919_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='careresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='fairresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='libresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='loyresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='sanresponses',
            old_name='userId',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='totals',
            old_name='userId',
            new_name='userid',
        ),
    ]