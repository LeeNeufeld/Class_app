# Generated by Django 2.2.2 on 2019-09-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0009_authresponses_libresponses_loyresponses_sanresponses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('care_harm', models.IntegerField()),
                ('care_harm_yes', models.IntegerField()),
                ('care_harm_no', models.IntegerField()),
                ('fairness_cheating', models.IntegerField()),
                ('fairness_cheating_yes', models.IntegerField()),
                ('fairness_cheating_no', models.IntegerField()),
                ('loyalty_betrayal', models.IntegerField()),
                ('loyalty_betrayal_yes', models.IntegerField()),
                ('loyalty_betrayal_no', models.IntegerField()),
                ('authority_subversion', models.IntegerField()),
                ('authority_subversion_yes', models.IntegerField()),
                ('authority_subversion_no', models.IntegerField()),
                ('sanctity_degradation', models.IntegerField()),
                ('sanctity_degradation_yes', models.IntegerField()),
                ('sanctity_degradation_no', models.IntegerField()),
                ('liberty_oppression', models.IntegerField()),
                ('liberty_oppression_yes', models.IntegerField()),
                ('liberty_oppression_no', models.IntegerField()),
            ],
        ),
    ]
