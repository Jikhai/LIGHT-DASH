# Generated by Django 2.1.5 on 2019-04-18 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightdash', '0013_linkydata10min_linkydatahour_linkydatamonth_linkydataweek'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkydata',
            name='iinst',
        ),
        migrations.RemoveField(
            model_name='linkydata10min',
            name='iinst',
        ),
        migrations.RemoveField(
            model_name='linkydatahour',
            name='iinst',
        ),
        migrations.RemoveField(
            model_name='linkydatamonth',
            name='iinst',
        ),
        migrations.RemoveField(
            model_name='linkydataweek',
            name='iinst',
        ),
    ]