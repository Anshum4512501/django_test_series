# Generated by Django 3.0.7 on 2020-07-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testseriesapp', '0003_auto_20200712_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='testseries',
            name='participent',
            field=models.ManyToManyField(through='testseriesapp.TestSeriesParticipents', to='testseriesapp.Participent'),
        ),
    ]