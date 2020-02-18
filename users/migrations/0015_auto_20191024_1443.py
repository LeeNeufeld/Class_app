# Generated by Django 2.2.2 on 2019-10-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20191024_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='urbanization',
            field=models.TextField(choices=[('Large urban centre (population 100,000 or more)', 'Large urban centre (population 100,000 or more)'), ('Medium population centres (population 30,000 to 99,999)', 'Medium population centres (population 30,000 to 99,999)'), ('Small population centres (population 1,000 to 29,999)', 'Small population centres (population 1,000 to 29,999)'), ('Rural Area', 'Rural Area')], null=True),
        ),
    ]
