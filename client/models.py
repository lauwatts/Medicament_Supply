# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
from django.db import models
from django.core import validators


class Client(models.Model):
    id_card = models.CharField(max_length=20, unique=True, validators=[validators.RegexValidator(re.compile('^[0-9]+$'), ('Numero no Valido'), 'invalid')])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=2, validators=[validators.RegexValidator(re.compile('^[0-9]+$'), ('Edad no Valida'), 'invalid')])

    def __str__(self):
		return self.first_name + " " + self.last_name
