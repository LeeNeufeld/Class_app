# Generated by Django 2.2.2 on 2019-09-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0006_auto_20190904_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='FairResponses',
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
        migrations.AlterField(
            model_name='responses',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
