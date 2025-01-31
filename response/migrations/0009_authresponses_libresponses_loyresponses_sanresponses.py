# Generated by Django 2.2.2 on 2019-09-12 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0008_auto_20190912_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sentence', models.TextField()),
                ('response', models.CharField(max_length=15, null=True)),
                ('userId', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sentence', models.TextField()),
                ('response', models.CharField(max_length=15, null=True)),
                ('userId', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoyResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sentence', models.TextField()),
                ('response', models.CharField(max_length=15, null=True)),
                ('userId', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SanResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('sentence', models.TextField()),
                ('response', models.CharField(max_length=15, null=True)),
                ('userId', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
