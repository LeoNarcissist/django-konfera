# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konfera', '0030_auto_20170129_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='title',
            field=models.CharField(blank=True, max_length=128, verbose_name='Name'),
        ),
    ]