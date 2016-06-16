# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from client.models import Client
from django.contrib.auth.models import User
from django.utils import timezone


class Medicament(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()


class Bill(models.Model):
    client = models.ForeignKey(Client)
    seller = models.ForeignKey(User)
    sale_date = models.DateTimeField(default=timezone.now)


class MedicamentBill(models.Model):
    bill = models.ForeignKey(Bill)
    medicament = models.ForeignKey(Medicament)
    amount = models.IntegerField()
