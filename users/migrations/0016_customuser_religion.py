# Generated by Django 2.2.2 on 2019-10-24 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20191024_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='religion',
            field=models.TextField(choices=[('Buddhist', 'Buddhist'), ('Christian', (('Anglican', 'Anglican'), ('Baptist', 'Baptist'), ('Catholic', 'Catholic'), ('Christian Orthodox', 'Christian Orthodox'), ('Lutheran', 'Lutheran'), ('Pentecostal', 'Pentecostal'), ('Presbyterian', 'Presbyterian'), ('United Church', 'United Church'), ('Other Christian', 'Other Christian'))), ('Hindu', 'Hindu'), ('Jewish', 'Jewish'), ('Muslim', 'Muslim'), ('Sikh', 'Sikh'), ('Traditional (Aboriginal) Spirituality', 'Traditional (Aboriginal) Spirituality'), ('Other religions', 'Other religions'), ('No religious affiliation', 'No religious affiliation')], null=True),
        ),
    ]
