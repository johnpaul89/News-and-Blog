# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuk', '0003_auto_20180907_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuk.User'),
        ),
    ]
