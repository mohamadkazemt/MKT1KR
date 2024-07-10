from django.shortcuts import render, get_object_or_404, redirect
from .models import Machine, Operation, Failure
from .forms import MachineForm

def machine_list(request):
    machines = Machine.objects.all()
    form = MachineForm()
    return render(request, 'Machine_app/machine_list.html', {'machines': machines, 'form': form})


def machine_detail(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    operations = machine.operations.all().order_by('-timestamp')
    failures = machine.failures.all().order_by('-timestamp')
    return render(request, 'Machine_app/machine_detail.html', {'machine': machine, 'operations': operations, 'failures': failures})

def machine_create(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
        else:
            machines = Machine.objects.all()
            return render(request, 'Machine_app/machine_list.html', {'machines': machines, 'form': form})
    else:
        return redirect('machine_list')

def machine_update(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm(instance=machine)
    return render(request, 'Machine_app/machine_form.html', {'form': form})

def machine_delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        machine.delete()
        return redirect('machine_list')
    return render(request, 'Machine_app/machine_confirm_delete.html', {'machine': machine})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Machine
from .forms import MachineForm

def machine_list(request):
    machines = Machine.objects.all()
    form = MachineForm()
    return render(request, 'Machine_app/machine_list.html', {'machines': machines, 'form': form})

def machine_create(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    return redirect('machine_list')

def machine_update(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    return redirect('machine_list')

def machine_delete(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    if request.method == "POST":
        machine.delete()
        return redirect('machine_list')
    return redirect('machine_list')

def machine_detail(request, pk):
    machine = get_object_or_404(Machine, pk=pk)
    return render(request, 'Machine_app/machine_detail.html', {'machine': machine})
