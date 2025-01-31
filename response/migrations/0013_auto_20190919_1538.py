# Generated by Django 2.2.2 on 2019-09-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response', '0012_auto_20190919_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totals',
            name='authority_subversion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='authority_subversion_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='authority_subversion_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='care_harm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='care_harm_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='care_harm_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='fairness_cheating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='fairness_cheating_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='fairness_cheating_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='liberty_oppression',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='liberty_oppression_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='liberty_oppression_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='loyalty_betrayal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='loyalty_betrayal_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='loyalty_betrayal_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='sanctity_degradation',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='sanctity_degradation_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='sanctity_degradation_yes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='totals',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
