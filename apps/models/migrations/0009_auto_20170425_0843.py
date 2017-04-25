# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 08:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_auto_20170425_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Gestor'),
        ),
    ]
