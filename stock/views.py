from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def add_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MedicamentForm()
    return render(request, 'medicament/add.html', {'form': form})


@login_required
def list_medicament(request):
    medicaments = Medicament.objects.all()
    return render(request, 'medicament/list.html', {'medicaments': medicaments})


@login_required
def edit_medicament(request, pk):
    medicament = get_object_or_404(Medicament, id=pk)
    if request.method == 'POST':
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
    else:
        form = MedicamentForm(instance=medicament)
    return render(request, 'medicament/add.html', {'form': form})


@login_required
def remove_medicament(request, pk):
    medicament = get_object_or_404(Medicament, id=pk)
    medicament.delete()
    return redirect(reverse('stock:list_medicament'))


@login_required
def add_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BillForm()
    return render(request, 'bill/add.html', {'form': form})


@login_required
def list_bill(request):
    bill = Bill.objects.all()
    return render(request, 'bill/list.html', {'bills': bill})


@login_required
def edit_bill(request, pk):
    bill = get_object_or_404(Bill, id=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
    else:
        form = BillForm(instance=medicament)
    return render(request, 'bill/add.html', {'form': form})


@login_required
def remove_bill(request, pk):
    bill = get_object_or_404(Bill, id=pk)
    bill.delete()
    return redirect(reverse('stock:list_bill'))
