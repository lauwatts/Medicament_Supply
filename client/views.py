from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
from .models import Client


@login_required
def add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm()
    return render(request, 'client/add.html', {'form': form})


@login_required
def list(request):
    Clients = Client.objects.all()
    return render(request, 'client/list.html', {'clients': Clients})


@login_required
def edit(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/add.html', {'form': form})


@login_required
def remove(request, pk):
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect(reverse('client:list'))
