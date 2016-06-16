# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 01:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'Numero no Valido', 'invalid')])),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[0-9]+$'), 'Edad no Valida', 'invalid')])),
            ],
        ),
    ]
