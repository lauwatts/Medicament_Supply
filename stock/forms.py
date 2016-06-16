# -*- coding: utf-8 -*-

from django import forms
from .models import *


class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ('name', 'amount', 'price')
        widgets = {
            # "picture_profile": forms.FileInput(attrs={'class': 'input-img-selector uk-align-center'}),
        }


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('client', 'seller')
        widgets = {
            # "picture_profile": forms.FileInput(attrs={'class': 'input-img-selector uk-align-center'}),
        }
