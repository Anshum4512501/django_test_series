# Generated by Django 3.0.7 on 2020-07-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testseriesapp', '0005_auto_20200714_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testseriesapp.Test'),
        ),
    ]
