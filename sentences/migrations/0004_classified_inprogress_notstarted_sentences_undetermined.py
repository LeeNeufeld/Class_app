# Generated by Django 2.2.2 on 2019-11-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentences', '0003_partyreleases_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('sentenceid', models.IntegerField(blank=True, null=True)),
                ('classification', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'classified',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('sentenceid', models.TextField(blank=True, null=True)),
                ('questionid', models.IntegerField(blank=True, null=True)),
                ('classification', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('educational_attainment', models.CharField(blank=True, max_length=100, null=True)),
                ('ethncity', models.CharField(blank=True, max_length=100, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('urbanization', models.CharField(blank=True, max_length=100, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'in_progress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotStarted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentenceid', models.IntegerField(blank=True, null=True)),
                ('confidence_score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'not_started',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sentences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('confidence_score', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('source_id', models.TextField(blank=True, null=True)),
                ('user_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sentences',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Undetermined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('sentenceid', models.IntegerField(blank=True, null=True)),
                ('classification', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'undetermined',
                'managed': False,
            },
        ),
    ]