# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20171012_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='Month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
    ]
