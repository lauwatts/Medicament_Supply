from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home.html')
