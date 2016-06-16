# -*- coding: utf-8 -*-

from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('id_card', 'first_name', 'last_name', 'age')
