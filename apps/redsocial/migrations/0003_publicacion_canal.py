# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0002_auto_20170210_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='canal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='redsocial.canal'),
        ),
    ]
